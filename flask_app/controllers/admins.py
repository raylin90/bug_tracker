# import Flask from __init__.py file
from flask_app import app
# import render_template(view HTML), redirect(route to different URL), request(get data from HTML), session(store session value), flask(display flash message
from flask import render_template,redirect,request,session, flash
from flask_app.models.admin import Admin

######################################
# view one admins account
######################################
@app.route("/view/admin/<id>")
def view_one_admin(id):
    # check if user has enough admin lvl to new the page
    if not session["admin_level"] or session["admin_level"] < 8:
        flash("Setting Page Only Open to Admin User")
        return redirect("/dashboard")
    data = {
        "id": int(id),
    }
    # fetch data from database
    one_admin = Admin.get_admins_by_user_id(data)
    print(one_admin)
    return render_template("admins/view_one_admin.html", one_admin = one_admin)

######################################
# activate admins account
######################################
@app.route("/activate/admin/<id>")
def activate_one_admin(id):
    # check if user has enough admin lvl to new the page
    if not session["admin_level"] or session["admin_level"] < 8:
        flash("Setting Page Only Open to Admin User")
        return redirect("/dashboard")
    data = {
        "id": int(id),
    }
    # fetch data from database
    one_admin = Admin.get_admins_by_user_id(data)
    return render_template("admins/activate_one_admin.html", one_admin = one_admin)

@app.route("/create/admin/<id>", methods = ["POST"])
def process_activate_admin_acct(id):
    data = {
        "id": int(id),
        "level_identifier": request.form["level_identifier"],
        "branch": request.form["branch"],
        "job_title": request.form["job_title"],
    }
    Admin.activate_admin(data)
    return redirect("/admins/setting")

######################################
# update admins account
######################################
@app.route("/edit/admin/<id>")
def edit_one_admin(id):
    # check if user has enough admin lvl to new the page
    if not session["admin_level"] or session["admin_level"] < 8:
        flash("Setting Page Only Open to Admin User")
        return redirect("/dashboard")
    data = {
        "id": int(id),
    }
    # fetch data from database
    one_admin = Admin.get_admins_by_user_id(data)
    return render_template("admins/edit_one_admin.html", one_admin = one_admin)

@app.route("/update/admin/<id>", methods = ["POST"])
def update_one_admin(id):
    print(request.form)
    data = { 
        "id": int(id),
        "first_name": request.form["first_name"],
        "last_name": request.form["last_name"],
        "email": request.form["email"],
        "password": request.form["password"],
        "level_identifier": request.form["level_identifier"],
        "branch": request.form["branch"],
        "job_title": request.form["job_title"],
    }
    Admin.update_admin_info(data)
    # print(request.form)
    return redirect(f"/view/admin/{id}")

######################################
# delete admins account
######################################
@app.route("/delete/admin/<id>")
def delete_one_admins(id):
    # check if user has enough admin lvl to new the page
    if not session["admin_level"] or session["admin_level"] < 8:
        flash("Setting Page Only Open to Admin User")
        return redirect("/dashboard")
    data = {
        "id": int(id),
        "lvl": int(0),
        "title": "null",
        "branch": "null",
    }
    Admin.deactivate_admin(data)
    return redirect("/admins/setting")