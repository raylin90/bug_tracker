# Python Flask web application that allows user to submit technical bug or change request

1. Entity Relationship Diagram:
    * only admin user can create/edit technical ticket
    * registered user can only leave comments
![ERD](/flask_app/static/images/ERD.png)

2. Wireframe:


Technic Used:
1. used Jinja2 template engine for front-end view page
2. used CSS for styling
3. used jQuery for extra functionality like click and hover
4. used AJAX for dynamic web page by allowing only portion of the page reload
5. used MySQL as database
6. used Bcrypt; Validation and regex for user security


Admin Level:

0 - Inactivate User
able to view, search, comment and change it's own password

1 - Activate User
create ticket and edit/update ticket crated by him/her

5 - Tech User
edit/update all the tickets

8 - Admin
9 - Top Level
able to set up admin information



What I learned:

I learned CSS Grid as first time, as it's very cool tool to position out 2-D layout by changing it's columns and rows
deeper understanding of DOM Manipulation, on how data transfer from HTML to JS and vice versa




What's the difficulty I had:
It was a lot more complicated than I imagined in the first place. Instead of just getting the number and performing the computation. We need to consider many edge cases like:
The front display is string, and backend we need to treat it as float
if the user didn't enter anything, and wants to perform the computation
what if the user enters decimal first without pressing the 0
what if user entered decimal multiple times
The biggest issue I faced was trying to make the number look nicer. For example: put a comma , to separate the number in every three digits like 1,000 instead of displaying 1000. Instead of applying it directly (using built-in toLocaleString) I had some issues when facing the decimal. So I need to split the number into an integer and decimal part, then apply toLocaleString on the integer part then concatenate back for display on the front end