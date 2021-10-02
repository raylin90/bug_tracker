# Python Flask web application that allows users to submit technical bugs or change request

1. Entity Relationship Diagram:
* user is required to login to perform additional function
* regular user cannot create ticket, only authorized user can, see below table for detail authority, as admin level increase, user gain more feature access
|User|Admin Level|Feature|
|---|---|---|
|un-register|None|able to view and search|
|registered|0 - Inactivate User|comment and change it's own password|
|registered|1 - Activate User|create ticket and edit/update own ticket|
|registered|5 - Tech User|edit/update all the tickets|
|registered|8/9 - Admin/Top Level|able to set up admin information|
![ERD](/flask_app/static/images/ERD.png)

2. Wireframe:
![wireframe](/flask_app/static/images/wireframe.png)

3. Technique Used:
* used Jinja2 template engine for front-end view page
* used CSS for styling
* used jQuery for extra functionality like click and hover
* used AJAX for dynamic web page refresh by allowing only portion of the page reload
* used MySQL as backend database
* used Bcrypt for user security
* used regex & validation to check user input and keep data consistent

4. What I learned:
* built full CRUD Python - Flask web application
* learned jQuery and AJAX on my own, made website more dynamic
* SQL query language
* database relationship setup 
* built my first wireframe:

5. What's the difficulty I had:
* relationship: as project growth, relationship became more complicated, and harder to maintain, I need to depend on the wireframe to setup all the relationship and query correctly
* SQL queries: how to maintain clean, and effective use of query became a problem. It's easy to create a new one every time, but not in a smart way. So I went back and combine some of the queries so I can re-use them (ex: LEFT JOIN queries)
* different user authority: it's not just assign a level to each user, instead, need to make sure each route are verifying login user correctly, and at HTML page, need to make sure button are displayed (based on the admin level, different user will see different button) correct with flash message