# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL
# import flask, so we can display flash message at HTML
from flask import flash

class Comment:
    def __init__(self,data):   # match to db table columns
        self.id = data['id']
        self.text = data['text']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ######################################
    # comment validation
    ######################################
    @staticmethod
    def validate_comment(data):
            is_valid = True # we assume this is true
            if len(data['text']) < 5:
                flash("Comment should be at least 5 characters long.")
                is_valid = False
            return is_valid
    
    ######################################
    # save comment
    ######################################
    @classmethod
    def save_comment(cls, data):
        query = "INSERT INTO comments (text, created_at, user_id, ticket_id) VALUES (%(text)s, NOW(), %(user_id)s, %(ticket_id)s)"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ######################################
    # get ALL comments in db
    ######################################
    @classmethod
    def get_all_comments(cls, data):
        query = "SELECT first_name, text, comments.created_at FROM comments LEFT JOIN users ON comments.user_id = users.id WHERE ticket_id = %(id)s;"
        return connectToMySQL("bug_tracker").query_db(query, data)
