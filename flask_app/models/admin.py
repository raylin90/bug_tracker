# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL
# import flask, so we can display flash message at HTML
from flask import flash

# model the class after the user table from our database
class Admin:
    # match to db table columns
    def __init__(self,data=""):
        self.id = data['id']
        self.level_identifier = data['level_identifier']
        self.branch = data['branch']
        self.job_title = data['job_title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    ############################################
    # method to check admins info. (below methods only open to lvl 9 user)
    ############################################
    @classmethod
    def get_admins_by_user_id(cls, data):
        query = "SELECT * FROM users LEFT JOIN admins ON users.id = admins.user_id WHERE users.id = %(id)s;"
        one_admins_info = connectToMySQL("bug_tracker").query_db(query, data)
        print(one_admins_info)
        return one_admins_info[0]
    
    ############################################
    # activate admin acct. by assigning default value (so we can insert to db, and update later)
    ############################################
    @classmethod
    def activate_admin(cls, data):
        query = "INSERT INTO admins (level_identifier, branch, job_title, created_at, user_id) VALUES (%(level_identifier)s, %(branch)s, %(job_title)s, NOW(), %(id)s);"
        return connectToMySQL("bug_tracker").query_db(query, data)

    ############################################
    # update admin info.
    ############################################
    @classmethod
    def update_admin_info(cls, data):
        # first query update table user
        query1 = "UPDATE users SET first_name = %(first_name)s, last_name=%(last_name)s, email=%(email)s, password = %(password)s, updated_at = NOW() WHERE users.id=%(id)s;"
        connectToMySQL("bug_tracker").query_db(query1, data)
        # second query update table admins
        query2 = "UPDATE admins SET level_identifier = %(level_identifier)s, branch=%(branch)s, job_title=%(job_title)s, user_id=%(id)s, updated_at = NOW() WHERE admins.user_id=%(id)s;"
        return connectToMySQL("bug_tracker").query_db(query2, data)

    ############################################
    # delete admin info.
    ############################################
    @classmethod
    def delete_admin(cls, data):
        query = "DELETE FROM admins WHERE admins.user_id=%(id)s"
        return connectToMySQL("bug_tracker").query_db(query, data)