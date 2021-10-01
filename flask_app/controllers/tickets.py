# import Flask from __init__.py file
from flask_app import app
# import render_template(view HTML), redirect(route to different URL), request(get data from HTML), session(store session value), flask(display flash message
from flask import render_template,redirect,request,session, flash, jsonify
from flask_app.models.ticket import Ticket
from flask_app.models.admin import Admin
from flask_app.models.user import User
from flask_app.models.comment import Comment

######################################
# create a new ticket
######################################
@app.route("/create_ticket")
def create_ticket():
    # get the admin info. by using their session id, we want to limit the create access to certain users only
    data = {
        "id": session["user_id"]
    }
    one_admin = Admin.get_admins_info(data)
    # if user is not authorized admin, redirect
    if not one_admin:
        flash("Create Ticket Page Only Open to Authorized User")
        return redirect("/dashboard")
    # print(one_admin["level_identifier"])
    session["admin_level"] = one_admin[0]["level_identifier"]
    session["admin_id"] = one_admin[0]["id"]
    # print(session["admin_id"])
    return render_template ("/tickets/create.html")

@app.route("/save_ticket", methods=["POST"])
def save_ticket():
    # validate ticket input
    if not Ticket.validate_ticket(request.form):
        return redirect('/create_ticket')

    # save ticket after validation
    data = {
        "id": session["admin_id"],
        "title": request.form["title"],
        "description": request.form["description"],
        "urgency": request.form["urgency"],
        "est_due_date": request.form["est_due_date"],
        "status": request.form["status"],
    }
    Ticket.save_ticket(data)
    return redirect ("/dashboard")

######################################
# view ticket route
######################################
@app.route("/view/ticket/<id>")
def view_ticket(id):
    data = {
        "id" : int(id),
    }
    # show pre-filled information for user's easy refeerence
    ticket = Ticket.show_one_ticket(data)
    print(ticket)
    return render_template("tickets/view.html", ticket = ticket)

######################################
# edit & update ticket route
######################################
@app.route("/edit/ticket/<id>")
def edit_ticket(id):
    data = {
        "id" : int(id),
    }
    ticket = Ticket.show_one_ticket(data)
    users = User.get_all_users()
    # print(users)
    # print(ticket["assigned_to"])
    comments = Comment.get_all_comments(data)
    print("1111111")
    print(comments)
    data = {
        "id": int(ticket["assigned_to"])
    }
    assigned_to_user = User.get_user_by_id(data)
    print("22222222")
    print(assigned_to_user)
    return render_template("tickets/edit.html", ticket = ticket, users = users, assigned_to_user = assigned_to_user, comments = comments)

@app.route("/update/ticket/<id>", methods=["POST"])
def update_ticket(id):
    data = {
        "title" : request.form["title"],
        "description" : request.form["description"],
        "urgency" : request.form["urgency"], 
        "est_due_date" : request.form["est_due_date"],
        "status" : request.form["status"],
        "assigned_to" : request.form["assigned_to"],
        "id" : int(id),
    }
    # validate ticket input
    if not Ticket.validate_ticket(data):
        return redirect(f'/edit/ticket/{id}')
    Ticket.update_one_ticket(data)
    return redirect("/dashboard")

######################################
# add comment for ticket
######################################
@app.route("/update/comment/<id>", methods=["POST"])
def update_comment(id):
    # validate comment input
    data = {
        "text": request.form["text"],
        "user_id": session["user_id"],
        "ticket_id": int(id)
    }
    if not Comment.validate_comment(data):
        return redirect(f'/edit/ticket/{id}')
    Comment.save_comment(data)
    return redirect("/dashboard")

######################################
# search ticket route
######################################
@app.route("/ajaxlivesearch", methods=["POST", "GET"])
def ajax_live_search():
    if request.method == "POST":
        # get search word from input
        data = {
            "search_word": request.form["query"]
        }
        # print(data["search_word"])
        tickets = Ticket.search_ticket(data)
    # serializes data into JSON format
    return jsonify(render_template("tickets/response.html", tickets = tickets))

@app.route("/livetablesort", methods=['GET', 'POST'])
def sort_table():
    data = {
        "search": request.form['query'],
    }
    # show pre-filled information for user's easy refeerence
    ticket = Ticket.sort_tickets(data)
    return jsonify(render_template("tickets/table.html", tickets = ticket))

######################################
# Analytics route (will show graph)
######################################
@app.route("/analytics")
def chart():
    # pending function, need to figuare out how to pass data from python to JS
    # using chart.js
    data = {
        "id": session["user_id"]
    }
    user = User.get_user_by_id(data)
    return render_template("tickets/chart.html", user = user)

######################################
# Category route (will show each ticket status)
######################################
@app.route("/tickets/status")
def show_table_by_category():
    # pending function, need to figuare out how to pass data from python to JS
    # using chart.js
    data = {
        "id": session["user_id"]
    }
    user = User.get_user_by_id(data)
    return render_template("tickets/category.html", user = user)

@app.route("/searchstatus", methods = ["POST"])
def process_category():
    data = {
        "search": request.form["query"]
    }
    print(request.form["query"])
    tickets = Ticket.search_by_status(data)
    count = Ticket.count_by_status(data)
    return jsonify(render_template("tickets/full-table.html", all_tickets = tickets, count = count[0]))