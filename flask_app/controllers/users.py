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
    if "user_id" in session:
        # get the user info when they login by using their session id
        data = {
            "id": session["user_id"]
        }
        user = User.get_user_by_id(data)
    else:
        user = ""
    return render_template("dashboard.html", user = user)

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
    # if user alrready at db, redirect user with flash message
    if user_in_db:
        flash("Email already in use, please use another email!")
        return redirect('/register')
    # validate if the input are matching to validation rule
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
    }
    # insert will return the id for data we just stored
    user_id = User.save_user(data)
    session["user_id"] = user_id
    return redirect("/")

######################################
# login route
######################################
@app.route("/login")
def login():
    return render_template("users/login.html")

@app.route("/login_user", methods = ["POST"])
def login_user():
    #validate if email already exist at db
    data = { 
        "email" : request.form["email"] 
    }
    user_in_db = User.get_user_by_email(data)
    # if user is not registered in the db
    if not user_in_db:
        flash("Invalid Login!!!")
        return redirect("/login")
    # if email exist at db, we check if hashed password matching or not
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Login!!!")
        return redirect('/login')
    # if the passwords matched, we set the user_id into session
    session['user_id'] = user_in_db.id
    return redirect("/")

######################################
# logout route
######################################
@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")

######################################
# change user pw route (only apply to registered user)
######################################
@app.route("/edit/user/<id>")
def edit_user(id):
    if "user_id" in session:
    # get the user info when they login by using their session id
        data = {
            "id": session["user_id"]
        }
        user = User.get_user_by_id(data)
    else:
        flash("please login before view profile")
        return redirect("/login")
    return render_template("users/edit_user.html", user = user)

@app.route("/update/user/<id>", methods = ["POST"])
def update_user(id):
    data = { 
        "id" : session["user_id"]
    }
    user_in_db = User.get_user_by_id(data)
    # check if old password matching to db or not
    if not bcrypt.check_password_hash(user_in_db.password, request.form['old_password']):
        # if we get False after checking the password
        flash("Old Password is not correct, please try again!!!")
        return redirect(f'/edit/user/{id}')
    # if above is good ,validate and hash the password
    if not User.validate_user(request.form):
        return redirect(f'/edit/user/{id}')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    # then save user info into database using prepared data dict.:
    data = {
        "password": pw_hash,
        "id" : session["user_id"]
    }
    print(pw_hash)
    User.update_user_password(data)
    return redirect("/")

# edge case if user tryint to click User btn before login sice no id param passed in
@app.route("/edit/user/")
def edit_user2():
    flash("please login before viewing user profile")
    return redirect("/login")