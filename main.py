# Team 3's Python driver
# This is the main driver for the project; hosts all methods, calls to database, as well as functionally runs the website.

from flask import Flask as fl
from flask import url_for, request, render_template
from markupsafe import escape

app = fl(__name__)


@app.route("/")
def homepage():
    pass #TODO: Obtain index.html and display it upon launch of webapp.

@app.route("/order", methods = ["GET", "POST"])
def placeOrder():
    pass #TODO: Obtain orderForm.html and add functionality.

