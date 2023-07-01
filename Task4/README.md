## Task 4: Add a button to re-fetch or re-load new tickets if any from Jira and put them into the database.

 Step 1: Import necessary modules

  from flask import Flask, redirect, render_template, request, url_for <br>
  import jira<br>
  from jira import JIRA<br>
  import MySQL.connector

 Step 2: Create a Flask application object
    A Flask application object is created using the Flask constructor. The __name__ variable represents the current module, and 
    template_folder is specified to locate the HTML templates.

Step 3: Define the login route
Step 4: Define the home route
Step 5: Define the learn route
Step 6: Define the check_schema route
  The @app.route('/check_schema') decorator defines the "check_schema" route. The check_schema() function handles the process of fetching Jira tickets and storing them in a MySQL database.
  The function first establishes a connection to the MySQL database and creates a new table named "new_data1" if it does not exist already.
 For each Jira issue, it extracts relevant data (Number, Name, Description, Reporter, Status, Due_date, Assignee).
If the issue number already exists in the database, the corresponding record is updated; otherwise, a new record is inserted.
The database is committed after each insertion or update.

step 7: Define the Main Driver Function:
    The if __name__ == '__main__': block ensures that the Flask application runs only if the script is executed directly, not when it is imported as a module. The app.run(debug=True) line starts the Flask development server on localhost, enabling debugging.



















