# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template, redirect, session
from markupsafe import escape
import mysql.connector
import re
import random
import time as t

# Initialize FLASK
app = fl(__name__, static_url_path='/static')
app.secret_key = "Team3Project"

# Database connection functions
def connectdb():
    try:
        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "mysql",
            database = "bakery"
        )
        print("Connected!")
        return mydb
    except:
        print("Connection failed, uh oh!")


def disconnectdb(mydb):
    mydb.close()


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/order", methods=["GET", "POST"])
def order():
    msg = ""
    # TODO: Test functionality
    if request.method == "POST" and "item" in request.form and "flavor" in request.form and "size" in request.form and "quantity" in request.form and "decorRequests" in request.form and "day" in request.form and "pickup" in request.form:
        items = request.form.getlist("item")
        flavors = request.form.getlist("flavor")
        sizes = request.form.getlist("size")
        quantities = request.form.getlist("quantity")
        requests = request.form.getlist("decorRequest")
        date = request.form["day"]
        time = request.form["pickup"]
        placed_time = t.localtime()
        timeString = t.strftime("%H:%M:%S", placed_time)
        orderConfirmation = 1 + (random.random() * 125478) #Such a large number that we can't possibly have repeats

        mydb = connectdb()
        cursor = mydb.cursor()
        if session["loggedin"] == True:
            cursor.execute("SELECT * FROM Account WHERE Email = %s",[(session["email"])])
            account = cursor.fetchone()
            cursor.execute("INSERT INTO Orders VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s)", (orderConfirmation, timeString, date, time, account[5], account[6], account[7], account[8]))
            for i in range(len(items)):
                cursor.execute("INSERT INTO OrderDetails VALUES(%s, %s, %s, %s, %s)", (orderConfirmation, items[i], sizes[i], flavors[i], quantities[i], requests[i]))
        else:
            msg = "You must be logged in to order! Please make an account and try again!"
            redirect(url_for("login"))
        mydb.commit()
        disconnectdb()
        msg = "Order Confirmation Number: %f".format(orderConfirmation)
    elif request.method == "POST":
        msg = "Sorry, something went wrong! Try reloading and ordering again!"

    return render_template("order.html", msg=msg)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    msg = ""
    if request.method == "POST" and "date" in request.form and "time" in request.form and "phone" in request.form and "email" in request.form and "question" in request.form:
        date = request.form["date"]
        time = request.form["time"]
        phone = request.form["phone"]
        email = request.form["email"]
        question = request.form["question"]
        mydb = connectdb()
        cursor = mydb.cursor()
        command = "INSERT INTO Contact (ContactDate, ContactTime, ContactPhone, ContactEmail, ContactQuestion) VALUES (%s, %s, %s, %s, %s)"
        values = (date, time, phone, email, question)
        cursor.execute(command, values)
        mydb.commit()
        # Testing below
        print(cursor.rowcount, " record inserted")
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST":
        msg = "There was an error handling your request, please try again!"
        # Testing below
        print(request.form, " List of all the data sent")

    return render_template("contact.html", msg=msg)

@app.route("/replyContact", methods=["GET", "POST"])
def replyContact():

    if 'employee' in session and session["employee"] != 1 or 'employee' not in session:
        print("You are not allowed to access this page!")
        return render_template("index.html")
    
    msg = ""

    try: 
        mydb = connectdb()
        cursor = mydb.cursor()

        cursor.execute('SELECT * from Contact')
        contact = cursor.fetchall()
    except:
        print("An error has occurred while displaying the contact table!")

    if request.method == "POST" and request.form["replyConfirm"] == "1":
        print(request.form)
        contactID = request.form["contactID"]
        replyMsg = request.form["replyMsg"]
        emailOption = request.form["emailOption"]
        cursor.execute("SELECT * FROM Contact WHERE ContactID = %s", [(contactID)])
        userContact = cursor.fetchone()
        print(userContact)
        if userContact:
            cursor.execute("DELETE from Contact WHERE ContactID = %s", [(contactID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry the ID inputted was not found!"
    elif request.method == "POST":
        msg = "Please fill out the information before submitting!"

    disconnectdb(mydb)

    return render_template("replyContact.html", msg=msg, contact=contact)

@app.route("/adminPage")
def adminPage():
    if 'employee' in session and session["employee"] == 1:
        return render_template("adminPage.html")
    else:
        print("You are not allowed to access this page!")
        return render_template("index.html")
        

@app.route("/menu")
def menu():
    try:
        mydb = connectdb()
        cursor = mydb.cursor()

        cursor.execute('SELECT * FROM minidesserts')
        miniMenu = cursor.fetchall()

        cursor.execute('SELECT * FROM desserttray')
        trays = cursor.fetchall()
    
        cursor.execute('SELECT * FROM pieandcheesecake')
        piecheese = cursor.fetchall()

        cursor.execute('SELECT * FROM cupcake')
        cupcake = cursor.fetchall()

        cursor.execute('SELECT * FROM dietary')
        dietary = cursor.fetchall()

        cursor.execute('SELECT * FROM signatureflavorcake')
        sf = cursor.fetchall()

        cursor.execute('SELECT * FROM cake')
        cake = cursor.fetchall()

        disconnectdb(mydb)
        return render_template("menu.html", miniMenu=miniMenu, trays=trays, piecheese=piecheese, cupcake=cupcake, dietary=dietary, sf=sf, cake=cake)
    except:
        print("An error has occurred while displaying the menu!")

# Admin Menu Functions below
# ADDING TO MENU
@app.route("/addMenu", methods=["GET", "POST"])
def addMenu():

    if 'employee' in session and session["employee"] != 1 or 'employee' not in session:
        print("You are not allowed to access this page!")
        return render_template("index.html")

    msg = ""
    if request.method == "POST" and request.form["menuID"] == "1":
        menuID = request.form["menuID"]
        categoryName = request.form["categoryName"]
        dessertName = request.form["dessertName"]
        dessertPrice = request.form["dessertPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO MiniDesserts (MenuID, CategoryName, DessertName, DessertPrice) VALUES (%s, %s, %s, %s)", (menuID, categoryName, dessertName, dessertPrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "2":
        menuID = request.form["menuID"]
        categoryName = request.form["categoryName"]
        sizeName = request.form["sizeName"]
        sizePrice = request.form["sizePrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO DessertTray (MenuID, CategoryName, SizeName, SizePrice) VALUES (%s, %s, %s, %s)", (menuID, categoryName, sizeName, sizePrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "3":
        menuID = request.form["menuID"]
        categoryName = request.form["categoryName"]
        PCName = request.form["PCName"]
        PCPrice = request.form["PCPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO PieAndCheesecake (MenuID, CategoryName, PCName, PCPrice) VALUES (%s, %s, %s, %s)", (menuID, categoryName, PCName, PCPrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "4":
        menuID = request.form["menuID"]
        sizeName = request.form["sizeName"]
        sizeDescription = request.form["sizeDescription"]
        cupcakePrice = request.form["cupcakePrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Cupcake (MenuID, SizeName, SizeDescription, CupcakePrice) VALUES (%s, %s, %s, %s)", (menuID, sizeName, sizeDescription, cupcakePrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "5":
        menuID = request.form["menuID"]
        categoryName = request.form["categoryName"]
        cakeSize = request.form["cakeSize"]
        dietaryPrice = request.form["dietaryPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Dietary (MenuID, CategoryName, CakeSize, DietaryPrice) VALUES (%s, %s, %s, %s)", (menuID, categoryName, cakeSize, dietaryPrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "6":
        menuID = request.form["menuID"]
        categoryName = request.form["categoryName"]
        cakeSize = request.form["cakeSize"]
        servings = request.form['servings']
        SFPrice = request.form["SFPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO SignatureFlavorCake (MenuID, CategoryName, CakeSize, Servings, SFPrice) VALUES (%s, %s, %s, %s, %s)", (menuID, categoryName, cakeSize, servings, SFPrice))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST" and request.form["menuID"] == "7":
        menuID = request.form["menuID"]
        cakeSize = request.form["cakeSize"]
        servings = request.form['servings']
        cakePrice = request.form['cakePrice']
        cakeEnhancement = request.form['cakeEnhancement']
        fillingEnhancement = request.form['fillingEnhancement']
        frostingEnhancement = request.form['frostingEnhancement']
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("INSERT INTO Cake (MenuID, CakeSize, Servings, CakePrice, CakeEnhancement, FillingEnhancement, FrostingEnhancement) VALUES (%s, %s, %s, %s, %s, %s, %s)", (menuID, cakeSize, servings, cakePrice, cakeEnhancement, fillingEnhancement, frostingEnhancement))
        mydb.commit()
        print(cursor.rowcount, " record inserted!") # TESTING
        disconnectdb(mydb)
        msg = "Form received! You may now exit this page."
    elif request.method == "POST":
        msg = "There was an error handling your request, please try again!"
        # Testing below
        print(request.form, " List of all the data sent")

    return render_template("addMenu.html", msg=msg)

# EDITING THE MENU
@app.route("/editMenu", methods=["GET", "POST"])
def editMenu():

    if 'employee' in session and session["employee"] != 1 or 'employee' not in session:
        print("You are not allowed to access this page!")
        return render_template("index.html")
    
    msg = ""

    try:
        mydb = connectdb()
        cursor = mydb.cursor()

        cursor.execute('SELECT * FROM minidesserts')
        miniMenu = cursor.fetchall()

        cursor.execute('SELECT * FROM desserttray')
        trays = cursor.fetchall()
        
        cursor.execute('SELECT * FROM pieandcheesecake')
        piecheese = cursor.fetchall()

        cursor.execute('SELECT * FROM cupcake')
        cupcake = cursor.fetchall()

        cursor.execute('SELECT * FROM dietary')
        dietary = cursor.fetchall()

        cursor.execute('SELECT * FROM signatureflavorcake')
        sf = cursor.fetchall()

        cursor.execute('SELECT * FROM cake')
        cake = cursor.fetchall()
    except:
        print("An error has occurred while displaying the table in editMenu!")

    if request.method == "POST" and request.form["menuID"] == "1":
        miniDessertsID = request.form["miniDessertsID"]
        categoryName = request.form["categoryName"]
        dessertName = request.form["dessertName"]
        dessertPrice = request.form["dessertPrice"]
        cursor.execute("SELECT * FROM MiniDesserts WHERE MiniDessertsID = %s", [(miniDessertsID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE MiniDesserts SET CategoryName = %s, DessertName = %s, DessertPrice = %s WHERE MiniDessertsID = %s", (categoryName, dessertName, dessertPrice, miniDessertsID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "2":
        dessertTrayID = request.form["dessertTrayID"]
        categoryName = request.form["categoryName"]
        sizeName = request.form["sizeName"]
        sizePrice = request.form["sizePrice"]
        cursor.execute("SELECT * FROM DessertTray WHERE DessertTrayID = %s", [(dessertTrayID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE DessertTray SET CategoryName = %s, SizeName = %s, SizePrice = %s WHERE DessertTrayID = %s", (categoryName, sizeName, sizePrice, dessertTrayID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "3":
        PCID = request.form["PCID"]
        categoryName = request.form["categoryName"]
        PCName = request.form["PCName"]
        PCPrice = request.form["PCPrice"]
        cursor.execute("SELECT * FROM PieAndCheesecake WHERE PCID = %s", [(PCID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE PieAndCheesecake SET CategoryName = %s, PCName = %s, PCPrice = %s WHERE PCID = %s", (categoryName, PCName, PCPrice, PCID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "4":
        cupcakeID = request.form["cupcakeID"]
        sizeName = request.form["sizeName"]
        sizeDescription = request.form["sizeDescription"]
        cupcakePrice = request.form["cupcakePrice"]
        cursor.execute("SELECT * FROM Cupcake WHERE CupcakeID = %s", [(cupcakeID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE Cupcake SET SizeName = %s, SizeDescription = %s, CupcakePrice = %s WHERE CupcakeID = %s", (sizeName, sizeDescription, cupcakePrice, cupcakeID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "5":
        dietaryID = request.form["dietaryID"]
        categoryName = request.form["categoryName"]
        cakeSize = request.form["cakeSize"]
        dietaryPrice = request.form["dietaryPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM Dietary WHERE dietaryID = %s", [(dietaryID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE Dietary SET CategoryName = %s, CakeSize = %s, DietaryPrice = %s WHERE dietaryID = %s", (categoryName, cakeSize, dietaryPrice, dietaryID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            disconnectdb(mydb)
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "6":
        SFID = request.form['SFID']
        categoryName = request.form["categoryName"]
        cakeSize = request.form["cakeSize"]
        servings = request.form['servings']
        SFPrice = request.form["SFPrice"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM signatureflavorcake WHERE SFID = %s", [(SFID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE signatureflavorcake SET CategoryName = %s, CakeSize = %s, servings = %s, SFPrice = %s WHERE SFID = %s", (categoryName, cakeSize, servings, SFPrice, SFID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            disconnectdb(mydb)
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "7":
        cakeID = request.form['cakeID']
        cakeSize = request.form["cakeSize"]
        servings = request.form['servings']
        cakePrice = request.form["cakePrice"]
        cakeEnhancement = request.form["cakeEnhancement"]
        fillingEnhancement = request.form["fillingEnhancement"]
        frostingEnhancement = request.form["frostingEnhancement"]
        mydb = connectdb()
        cursor = mydb.cursor()
        cursor.execute("SELECT * FROM cake WHERE cakeID = %s", [(cakeID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("UPDATE cake SET CakeSize = %s, servings = %s, cakePrice = %s, cakeEnhancement = %s, fillingEnhancement = %s, frostingEnhancement = %s WHERE cakeID = %s", (cakeSize, servings, cakePrice, cakeEnhancement, fillingEnhancement, frostingEnhancement, cakeID))
            mydb.commit()
            print(cursor.rowcount, " record updated!") # TESTING
            disconnectdb(mydb)
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST":
        msg = "There was an error handling your request, please try again!"
        # Testing below
        print(request.form, " List of all the data sent")

    disconnectdb(mydb)

    return render_template("editMenu.html", msg=msg, miniMenu=miniMenu, trays=trays, piecheese=piecheese, cupcake=cupcake, dietary=dietary, sf=sf,cake=cake)

# DELETING FROM MENU
@app.route("/deleteMenu", methods=["GET", "POST"])
def deleteMenu():

    if 'employee' in session and session["employee"] != 1 or 'employee' not in session:
        print("You are not allowed to access this page!")
        return render_template("index.html")
    
    msg = ""

    try:
        mydb = connectdb()
        cursor = mydb.cursor()

        cursor.execute('SELECT * FROM minidesserts')
        miniMenu = cursor.fetchall()

        cursor.execute('SELECT * FROM desserttray')
        trays = cursor.fetchall()
        
        cursor.execute('SELECT * FROM pieandcheesecake')
        piecheese = cursor.fetchall()

        cursor.execute('SELECT * FROM cupcake')
        cupcake = cursor.fetchall()

        cursor.execute('SELECT * FROM dietary')
        dietary = cursor.fetchall()

        cursor.execute('SELECT * FROM signatureflavorcake')
        sf = cursor.fetchall()

        cursor.execute('SELECT * FROM cake')
        cake = cursor.fetchall()
    except:
        print("An error has occurred while displaying the table in deleteMenu!")

    if request.method == "POST" and request.form["menuID"] == "1": 
        minidessertsID = request.form["miniDessertsID"]
        cursor.execute("SELECT * FROM minidesserts WHERE miniDessertsID = %s", [(minidessertsID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from minidesserts WHERE miniDessertsID = %s", [(minidessertsID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "2":
        dessertTrayID = request.form["dessertTrayID"]
        cursor.execute("SELECT * FROM DessertTray WHERE DessertTrayID = %s", [(dessertTrayID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from DessertTray WHERE DessertTrayID = %s", [(dessertTrayID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "3":
        PCID = request.form["PCID"]
        cursor.execute("SELECT * FROM PieAndCheesecake WHERE PCID = %s", [(PCID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from PieAndCheesecake WHERE PCID = %s", [(PCID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "4":
        cupcakeID = request.form["cupcakeID"]
        cursor.execute("SELECT * FROM Cupcake WHERE CupcakeID = %s", [(cupcakeID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from Cupcake WHERE CupcakeID = %s", [(cupcakeID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "5":
        dietaryID = request.form["dietaryID"]
        cursor.execute("SELECT * FROM dietary WHERE dietaryID = %s", [(dietaryID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from dietary WHERE dietaryID = %s", [(dietaryID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "6":
        SFID = request.form["SFID"]
        cursor.execute("SELECT * FROM SignatureFlavorCake WHERE SFID = %s", [(SFID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from SignatureFlavorCake WHERE SFID = %s", [(SFID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST" and request.form["menuID"] == "7":
        cakeID = request.form["cakeID"]
        cursor.execute("SELECT * FROM Cake WHERE cakeID = %s", [(cakeID)])
        item = cursor.fetchone()
        if item:
            cursor.execute("DELETE from Cake WHERE cakeID = %s", [(cakeID)])
            mydb.commit()
            print(cursor.rowcount, " record deleted!") # TESTING
            msg = "Form received! You may now exit this page."
        else:
            msg = "Sorry, the ID inputted was not found!"
    elif request.method == "POST":
        msg = "There was an error handling your request, please try again!"
        # Testing below
        print(request.form, " List of all the data sent")

    disconnectdb(mydb)

    return render_template("deleteMenu.html", msg=msg, miniMenu=miniMenu, trays=trays, piecheese=piecheese, cupcake=cupcake, dietary=dietary, sf=sf,cake=cake)

@app.route("/register", methods=["GET", "POST"])
def register():
    msg = ""
    mydb = connectdb()
    cursor = mydb.cursor()

    if request.method == "POST" and "password" in request.form and "email" in request.form and "firstname" in request.form and "lastname" in request.form and "phone" in request.form:
        password = request.form["password"]
        email = request.form["email"]
        firstname = request.form["firstname"]
        lastname = request.form["lastname"]
        phone = request.form["phone"]
        cursor.execute("SELECT * FROM ACCOUNT WHERE Email = %s", [(email)])
        account = cursor.fetchone()
        if account:
            msg = "Account already exists, login to your account!"
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = "Invalid email! Try again!"
        elif not password or not email:
            msg = "Incomplete form, please try again."
        else:
            cursor.execute("INSERT INTO ACCOUNT (Firstname, Lastname, Password, Email, Phone) VALUES(%s, %s, %s, %s, %s)", (firstname, lastname, password, email, phone))
            mydb.commit()
            msg = "Sucessfully registered! You may now login!"
            disconnectdb(mydb)
            return redirect(url_for("login"))
    elif request.method == "POST":
        msg = "Please fill out the information before submitting!"
    return render_template("register.html", msg = msg)

@app.route("/login", methods = ["GET", "POST"])
def login():
    msg = ""
    mydb = connectdb()
    cursor = mydb.cursor()
    
    if request.method == "POST" and "email" in request.form and "password" in request.form:
        email = request.form["email"]
        password = request.form["password"]
        cursor.execute("SELECT * FROM ACCOUNT WHERE Email = %s AND Password = %s", (email, password))
        account = cursor.fetchone()
        if account and account[6] == 0:
            session["loggedin"] = True
            session["id"] = account[0]
            session["email"] = email
            session["employee"] = account[6]
            msg = "Sucessfully logged in! You may now order!"
            disconnectdb(mydb)
            return redirect(url_for("order"))
        elif account and account[6] == 1:
            session["loggedin"] = True
            session["id"] = account[0]
            session["email"] = email
            session["employee"] = account[6]
            msg = "Sucessfully logged in! Redirecting to Admin page!"
            disconnectdb(mydb)
            return redirect(url_for("adminPage"))
        else:
            msg = "Incorrect login!"

    return render_template("login.html", msg = msg)

@app.route("/logout")
def logout():
    #TODO: Allow logging out and removal of session data (non priority)

    if 'loggedin' in session and session["loggedin"] == True:
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('email', None)
        session.pop('employee', None)
        print("You've been logged out!")
    else:
        print("You're not logged in!")

    return redirect(url_for('login'))

#This stores whether or not the user is logged in, and in the navbar html it shows the conditionality
#So, when the user is logged in they will see the "profile" button, not "sign in" and "register"
@app.route('/navbar')
def render_navbar():
    if 'loggedin' in session and session["loggedin"] == True:
        return render_template('navbar.html', logged_in=True)
    else:
        return render_template('navbar.html', logged_in=False)

@app.route("/profile")
def profile():
    #TODO: Test functionality
    mydb = connectdb()
    cursor = mydb.cursor()
    try:
        cursor.execute("SELECT * FROM Account WHERE Email = %s", (session["email"]))
        account = cursor.fetchone()
        return render_template("profile.html", account = account)
    except:
        print("An error has occurred while displaying your profile!")
    finally:
        disconnectdb(mydb)

@app.route('/viewOrder')
def viewOrder():
    # Most recent Order
    #TODO: Test functionality, and account for all previous orders
    mydb = connectdb()
    cursor = mydb.cursor()

    try:
        #Might have to do an if statement for when user is an admin, it selects all
        #orders from every customer and sorts by date. That way admins can see all orders
        cursor.execute("SELECT * FROM Orders WHERE CustomerEmail = %s", (session["email"]))
        order = cursor.fetchone()
        cursor.execute("SELECT * FROM OrderDetails WHERE ConfirmationNumber = %s", (order[1]))
        orderInfo = cursor.fetchall()
        return render_template("viewOrder.html", orderHistory = orderInfo)
    except:
        print("An error has occurred while displaying your orders!")
    finally:
        disconnectdb(mydb)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/galleryphotos")
def galleryphotos():
    return render_template("galleryphotos.html")

if __name__ == '__main__':
    app.run()