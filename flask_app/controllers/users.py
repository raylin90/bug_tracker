# import Flask from __init__.py file
from flask_app import app
# import render_template(view HTML), redirect(route to different URL), request(get data from HTML), session(store session value), flask(display flash message
from flask import render_template,redirect,request,session, flash

######################################
# dashboard route
######################################
@app.route("/")
def dashboard():
    return render_template("dashboard.html")

######################################
# register route
######################################
@app.route("/register")
def register():
    return render_template("users/register.html")