# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL
# import flask, so we can display flash message at HTML
from flask import flash, session

class Ticket:
    def __init__(self,data):   # match to db table columns
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.urgency = data['urgency']
        self.est_due_date = data['est_due_date']
        self.status = data['status']
        self.assigned_to = data['assigned_to']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ######################################
    # ticket validation
    ######################################
    @staticmethod
    def validate_ticket(data):
            is_valid = True # we assume this is true
            if len(data['title']) < 5:
                flash("Ticket title should be at least 5 characters long.")
                is_valid = False
            if len(data['description']) < 5:
                flash("Description should be at least 5 characters long.")
                is_valid = False
            return is_valid

    ######################################
    # save ticket after vallidation
    ######################################
    @classmethod
    def save_ticket(cls, data):
        query = "INSERT INTO tickets (title, description, urgency, est_due_date, status, created_at, admin_id) VALUES (%(title)s, %(description)s, %(urgency)s, %(est_due_date)s, %(status)s, NOW(), %(id)s);"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ######################################
    # show ALL tickets
    ######################################
    @classmethod
    def show_all_tickets(cls):
        query = "SELECT tickets.id, title, description, urgency, DATE_FORMAT(est_due_date, '%m-%d-%Y') AS est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed';"
        results = connectToMySQL("bug_tracker").query_db(query)
        return results

    ######################################
    # retrieve ONE ticket
    ######################################
    @classmethod
    def show_one_ticket(cls, data):
        query = "SELECT * FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE tickets.id = %(id)s;"
        ticket = connectToMySQL("bug_tracker").query_db(query, data)
        return ticket[0]

    ######################################
    # update ticket
    ######################################
    @classmethod
    def update_one_ticket(cls, data):
        query = "UPDATE tickets SET title = %(title)s, description = %(description)s, urgency = %(urgency)s, est_due_date = %(est_due_date)s, status= %(status)s, assigned_to= %(assigned_to)s, updated_at= NOW() WHERE tickets.id=%(id)s;"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ######################################
    # show data by ticket status
    ######################################
    @classmethod
    def search_by_status(cls, data):
        query = "SELECT tickets.id, title, description, urgency, est_due_date, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status = %(search)s;"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ######################################
    # count data by ticket status
    ######################################
    @classmethod
    def count_by_status(cls, data):
        query = "SELECT COUNT(tickets.id) AS count FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status = %(search)s;"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ######################################
    # search ticket
    ######################################
    @classmethod
    def search_ticket(cls, data):
        query = "SELECT * FROM tickets WHERE id LIKE %(search_word)s OR title LIKE %(search_word)s;"
        result = connectToMySQL("bug_tracker").query_db(query, data)
        # print(result)
        return result

    @classmethod
    def sort_tickets(cls, data):
        if "count" in session:
            if session["count"] == 1:
                session["count"] -= 1
            else:
                session["count"] += 1
        else:
            session["count"] = 0
        print(session["count"])
        if session["count"] == 1:
            if data['search'] == "id":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY tickets.id DESC;"
            elif data['search'] == "title":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY title DESC;"
            elif data['search'] == "urgency":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency DESC;"
            elif data['search'] == "admin_id":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY admin_id DESC;"
            elif data['search'] == "est_due_date":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency DESC;"
            elif data['search'] == "est_due_date":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency DESC;"
            elif data['search'] == "status":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY status DESC;"
            elif data['search'] == "timeline":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY time_line DESC;"
        else:
            if data['search'] == "id":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY tickets.id ASC;"
            elif data['search'] == "title":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY title ASC;"
            elif data['search'] == "urgency":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency ASC;"
            elif data['search'] == "admin_id":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY admin_id ASC;"
            elif data['search'] == "est_due_date":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency ASC;"
            elif data['search'] == "est_due_date":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY urgency ASC;"
            elif data['search'] == "status":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY status ASC;"
            elif data['search'] == "timeline":
                query = "SELECT tickets.id, title, description, urgency, est_due_date, DATEDIFF(est_due_date, NOW()) AS time_line, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id WHERE status !='Closed' ORDER BY time_line ASC;"
        tickets = connectToMySQL("bug_tracker").query_db(query, data)
        print(tickets)
        return tickets