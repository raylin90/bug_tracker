# import Flask to allow us to create our app
from flask import Flask
# create a new instance of the Flask class called "app"
app = Flask(__name__)
# session secret key
app.secret_key = '3;4qp!3@4&)3.5gfs4s6'