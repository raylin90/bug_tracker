# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL
# import flask, so we can display flash message at HTML
from flask import flash
# import regex for pattern validation
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z]+$')


# model the class after the user table from our database
class User:
    # match to db table columns
    def __init__(self,data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ############################################
    # validation registration input method
    ############################################
    @staticmethod
    def validate_user(data):
        is_valid = True
        if not NAME_REGEX.match(data['first_name']) or len(data['first_name']) < 2:
            flash("First name should contain letters only and at least 2 characters.")
            is_valid = False
        if not NAME_REGEX.match(data['last_name']) or len(data['last_name']) < 2:
            flash("Last name should contain letters only and at least 2 characters.") 
            is_valid = False
        if not EMAIL_REGEX.match(data['email']): 
            flash("Invalid email format!")
            is_valid = False
        if len(data['password']) < 8:
            flash("Password should be at least 8 characters.") 
            is_valid = False
        if data['password'] != data['conf_password']:
            flash("Password and Confirm Password does not match.") 
            is_valid = False
        return is_valid

    ############################################
    # method to check if user's email in db or not
    ############################################
    @classmethod
    def get_user_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        result = connectToMySQL("bug_tracker").query_db(query, data)
        if len(result) < 1:
            return False
        return cls(result[0])
    
    ############################################
    # method to save user's registration info.
    ############################################
    @classmethod
    def save_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, password, created_at) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, NOW())"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ############################################
    # get the user whom logged in
    ############################################
    @classmethod
    def get_user_by_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN admins ON users.id = admins.user_id WHERE users.id = %(id)s"
        login_user = connectToMySQL("bug_tracker").query_db(query, data)
        # print(results)
        # return results
        return cls(login_user[0])
    
    ############################################
    # update user password
    ############################################
    @classmethod
    def update_user_password(cls, data):
        query = "UPDATE users SET password = %(password)s, updated_at = NOW() WHERE id=%(id)s;"
        print("hi")
        return connectToMySQL("bug_tracker").query_db(query, data)
    
    ############################################
    # get all users with their admins setting
    ############################################
    @classmethod
    def get_users_admins_setting(cls):
        query = "SELECT * FROM users LEFT JOIN admins ON users.id = admins.user_id;"
        # results will be a list of dictionary
        user_with_admins_info = connectToMySQL("bug_tracker").query_db(query)
        return user_with_admins_info

    ############################################
    # get all users
    ############################################
    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users;"
        # results will be a list of dictionary
        users = connectToMySQL("bug_tracker").query_db(query)
        return users