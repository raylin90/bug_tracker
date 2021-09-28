# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL
# import flask, so we can display flash message at HTML
from flask import flash

class Ticket:
    def __init__(self,data):   # match to db table columns
        self.id = data['id']
        self.title = data['title']
        self.description = data['description']
        self.urgency = data['urgency']
        self.est_due_date = data['est_due_date']
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
        query = "SELECT tickets.id, title, description, urgency, DATE_FORMAT(est_due_date, '%M %D %Y') AS est_due_date, status, first_name FROM tickets LEFT JOIN admins ON tickets.admin_id = admins.id LEFT JOIN users ON admins.user_id = users.id;"
        results = connectToMySQL("bug_tracker").query_db(query)
        return results[0]

# ######################################
# # retrieve ONE ticket
# ######################################
#     @classmethod
#     def show_one_ticket(cls, data):
#         query = "SELECT * FROM tickets JOIN users ON tickets.user_id = users.id WHERE tickets.id=%(id)s;"
#         ticket = connectToMySQL("bug_tracker_schema").query_db(query, data)
#         return ticket[0]

# ######################################
# # update ticket
# ######################################
#     @classmethod
#     def update_one_ticket(cls, data):
#         query = "UPDATE tickets SET name = %(name)s, description = %(description)s, urgency = %(urgency)s, est_due_date = %(est_due_date)s, status= %(status)s WHERE tickets.id=%(id)s;"
#         return connectToMySQL("bug_tracker_schema").query_db(query, data)

# ######################################
# # search ticket
# ######################################
#     @classmethod
#     def search_ticket(cls, data):
#         query = "SELECT * FROM tickets WHERE name LIKE %(name)s;"
#         result = connectToMySQL("bug_tracker_schema").query_db(query, data)
#         print("+++++++++++++++++++++++++++++++")
#         return result
