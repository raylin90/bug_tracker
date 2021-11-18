# Bug Tracker
Python Flask web application that allow users to submit technical bugs or change requests

------------------
### Entity Relationship Diagram:
* user is required to login to perform additional function
* regular user cannot create ticket, only authorized user can, see below table for detail authority, as admin level increase, user gain more feature access

| User | Admin Level | Feature |
| --- | --- | --- |
| un-register | None | able to view and search|
| registered | 0 - Inactivate User | comment and change it's own password|
| registered | 1 - Activate User | create ticket and edit/update it's own ticket|
| registered | 5 - Tech User | edit/update all the tickets|
| registered | 8/9 - Admin/Top Level | able to set up admin information|
![ERD](/flask_app/static/images/ERD.png)

------------------
### Wireframe:
![wireframe](/flask_app/static/images/bug_tracker_wireframe.png)

------------------
### Tech/framework used
__Built with__
- Jinja2 template engine for front-end view page
- CSS for styling
- jQuery for extra functionality like click and hover
- AJAX for dynamic web page refresh by allowing only portion of the page reload
- MySQL as backend database
- Bcrypt for user security
- regex & validation to check user input and keep data consistent

------------------
### Spotlights:
1. built full CRUD Python - Flask web application
2. learned jQuery and AJAX on my own, made website more dynamic
3. SQL query language
4. database relationship setup 
5. built my first wireframe:
6. AWS Deployment using Gunicorn, Nginx

------------------
### Difficulties:
1. relationship: as the project scales up, relationships become more complicated, and harder to maintain, I need to rely on the wireframe to set up all the relationships and query correctly
2. SQL queries: how to maintain clean, and effective use of query became a problem. It's easy to create a new one every time, but not in a smart way. So I went back and combined some of the queries so I can re-use them (ex: LEFT JOIN queries)
3. different user authority: it's not just assign a level to each user, instead, need to make sure each route are verifying login user correctly, and at HTML page, need to make sure button are displayed (based on the admin level, different user will see different button) correct with flash message

------------------
### AWS(EC2) Deployment
http://3.135.1.254

L: r@l.com\
P: sdfsdfsdf\
you can use my admin account to test out features

------------------
### Installation
```
# Dump below ERD into your sql database
bug_tracker/ERD/bug_tracker.mwb

# Clone this repository
$ git clone https://github.com/raylin90/bug_tracker.git

# Go into the repository
$ cd bug_tracker

# Open in your editor
$ code . (I use VS Code, so it's the shortcut terminal command)

# Install Flask & MySQL connection
$ pipenv install PyMySQL flask

# Run virtual environment
$ pipenv shell
# if your terminal command  starts with (project name), then you are in virtual environment

# Run the app
$ python3 server.py
```
