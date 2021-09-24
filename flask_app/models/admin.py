# import mysqlconnection, so we can connecto SQL database
from flask_app.config.mysqlconnection import connectToMySQL

# model the class after the user table from our database
class Admin:
    # match to db table columns
    def __init__(self,data):
        self.id = data['id']
        self.level_identifier = data['level_identifier']
        self.branch = data['branch']
        self.job_title = data['job_title']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    # @classmethod
    # def get_users_admins_setting(cls):
    #     query = "SELECT * FROM users LEFT JOIN admins ON users.id = admins.user_id;"
    #     user_with_admins_info = connectToMySQL("bug_tracker").query_db(query)
    #     print(type(user_with_admins_info))
    #     return cls(user_with_admins_info)