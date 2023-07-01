## Task 4: Add a button to re-fetch or re-load new tickets if any from Jira and put them into the database.
# Html/css/javascript
   # Step 1: HTML Structure
     This is a basic HTML template that creates a page with a button to fetch Jira tickets and a placeholder to display the result.
   # step 2: Step 2: CSS Styles
      This CSS section adds some styles to the elements on the page. It styles the body with Arial font, centers the h2 heading, and defines styles for the button and message div.
   # Step 3: HTML Body Content
         The content inside the body tag contains a div with the class "container" to center the elements. Inside this div, there is an h2 heading that displays "Jira Ticket Fetcher" as the page title. Below the heading, there is a button with the class "button." This button, when clicked, calls the fetchTickets() JavaScript function. The p tag with the id="message" will display the result after fetching the tickets.

  # Step 4: JavaScript Function
  The <script> element contains the JavaScript code.
The fetchTickets() function is triggered when the button is clicked.
Inside the function, an XMLHttpRequest object is created.
The onreadystatechange event listener is set to handle the response from the server.
If the request is completed (readyState === 4) and the status is OK (status === 200), the message "Tickets fetched and stored successfully!" is displayed in the <p> element.
The XMLHttpRequest is then opened with the method "GET" and the URL "/check_schema". It is set to asynchronous mode (true).
Finally, the request is sent using the send() method

   # Flask code
   # Step 1: Import necessary modules
   
     from flask import Flask, redirect, render_template, request, url_for <br>
     import jira<br>
     from jira import JIRA<br>
     import MySQL.connector
   
   # Step 2: Create a Flask application object
       A Flask application object is created using the Flask constructor. The __name__ variable represents the current module, and 
       template_folder is specified to locate the HTML templates.
   
   # Step 3: Define the login route
   # Step 4: Define the home route
   # Step 5: Define the learn route
   # Step 6: Define the check_schema route
     The @app.route('/check_schema') decorator defines the "check_schema" route. The check_schema() function handles the process of fetching Jira tickets and storing them in a MySQL database.
     The function first establishes a connection to the MySQL database and creates a new table named "new_data1" if it does not exist already.
    For each Jira issue, it extracts relevant data (Number, Name, Description, Reporter, Status, Due_date, Assignee).
   If the issue number already exists in the database, the corresponding record is updated; otherwise, a new record is inserted.
   The database is committed after each insertion or update.
   
  # step 7: Define the Main Driver Function:
       The if __name__ == '__main__': block ensures that the Flask application runs only if the script is executed directly, not when it is imported as a module. The app.run(debug=True) line starts the Flask development server on localhost, enabling debugging.
   
  # Final Output:
    When we run the Html file in UI button has been created and when we clicked the button the massesge is printed yes insert succesfully and in the database final output be like:
         |Number|Name|Description|Reporter|Status|Due_date|Assigne|
         | :-------| :-------|:-------| :-------| :-------| :-------|:-------|
         |JAYAS-1|ticket-1|test55|Jaya Srivastava|Done|None|jaya Srivastava
         |JAYAS-6|for test only-python|just for practice|jaya Srivastava|In Progress|2024-04-19|None
         |JAYAS-3|ticket-3|just for checking|Jaya Srivastava|Done|None|jaya Srivastava|
   




















