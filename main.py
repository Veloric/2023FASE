# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template, redirect
from markupsafe import escape
import mysql.connector as msql

#Database connection set up
#mydb = msql.connect(
 #   host = "localhost",
 #   user = "root",
 #   password = "root"
#)

app = fl(__name__)


@app.route("/")
def homepage():
    return render_template("index.html")

@app.route("/order", methods = ["GET", "POST"])
def placeOrder(order):
    return render_template(url_for("order.html"))



if __name__ == '__main__':
    app.run()