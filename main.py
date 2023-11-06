# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template, redirect
from markupsafe import escape
import mysql.connector

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
    if request.method == "POST" and "flavor" in request.form and "size" in request.form and "quantity" in request.form and "decor" in request.form:
        flavor = request.form["flavor"]
        size = request.form["size"]
        quantity = request.form["quantity"]
        decor = request.form["decor"]
        mydb = connectdb()
        cursor = mydb.cursor()
        command = "INSERT INTO Orders (CupcakeFlavor, CupcakeSize, CupcakeQuantity, DecorRequests) VALUES (%s, %s, %s, %s)"
        values = (flavor, size, quantity, decor)
        cursor.execute(command, values)
        mydb.commit()
        # for testing purposes only
        print(cursor.rowcount, " record inserted")
        disconnectdb(mydb)
        msg = "Order placed! You may now exit this page. (Create an account to view order history)"
    elif request.method == "POST":
        msg = "There was an error handling your request, please try again!"
        # Testing purposes only
        print(request.form, " List of all data sent")
        
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

@app.route("/menu")
def menu():
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


@app.route("/register")
def register():
    return render_template("register.html")

# We don't have a login.html in templates/ yet
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()