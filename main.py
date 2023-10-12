# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template, redirect
from markupsafe import escape
# import mysql.connector as msql

#Database connection set up
#mydb = msql.connect(
 #   host = "localhost",
 #   user = "root",
 #   password = "root"
#)

app = fl(__name__, static_url_path='/static')
app.secret_key = "Team3Project"


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/order", methods=("GET", "POST"))
def order():
    if request.method == "POST":
        flavor = request.form.get("flavor")
        size = request.form.get("size")
        quantity = request.form.get("quantity")
        decor = request.form.get("decor")
        pass
    #TODO: Send data to database
    #TODO: Actually set up database

    return render_template("order.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/register")
def register():
    return render_template("register.html")

# We don't have a login.html in templates/ yet
@app.route("/login")
def login():
    return render_template("login.html")

if __name__ == '__main__':
    app.run()