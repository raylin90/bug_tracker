# import Flask from __init__.py fil
from flask_app import app
# import modules from controllers
from flask_app.controllers import users


# ensure this file is being run directly and not from different module
if __name__ == "__main__":
	app.run(debug=True)