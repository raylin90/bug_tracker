# import Flask from __init__.py file
from flask_app import app
# import render_template(view HTML), redirect(route to different URL), request(get data from HTML), session(store session value), flask(display flash message
from flask import render_template,redirect,request,session, flash
from flask_app.models.user import User
# Bcrypt to hash the password
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

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

@app.route("/create_user", methods = ["POST"])
def create_user():
    #validate if email already exist at db
    data = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.get_user_by_email(data)
    if user_in_db:
        flash("Email already in use, please use another email!")
        return redirect('/register')
    #validate if the input are matching the validation rule
    if not User.validate_user(request.form):
        return redirect('/register')
    # if no errors, we hash the password
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # then save user info into database using prepared data dict.:
    data = {
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": pw_hash,
        "admin_id": 0,
    }
    User.save_user(data)
    return redirect("/")