## Task 3: Create a UI to show the tickets from the database:-

   I fetch or access data from MySQL using Python and Flask Web Framework

## Run HTML Page in Python [Flask Web Framework] Website in Python
  
  Step 1: Create a project in PyCharm you can create this in any drive of your system. <br />
  Step 2: Create a template and static folders in your project.<br />
  Step 3: Create HTML page inside template folder.<br />
  Step 4: Create a HTML page.<br />
  Step 5: Create python file to execute this HTML file.<br />
  Step 6: Install Flask Library or Package.<br />
  Step 7: i write Python Code.<br />
  
## Insert/Store Data in MySQL using Flask
  step1: Create a dataase.<br />
  step2: create a table in mysql workbench.<br />
  step3: Need to install following libraries to communicate python with MySQL<br />
       Flask<br />
       Flask-MySQLdb<br />
       mysql<br />
       mysql-connector<br />
       
 ## Commands for Installation

For connect mysql to flask
```bash
   pip install Flask-MySQLdb
   pip install Flask
```

```bash
   pip install mysql
   pip install mysql-connector
```

# Html/Css code 
Step1: HTML Structure: <br/>

The code starts with the <!DOCTYPE html> declaration, which specifies that the document is an HTML5 document.
The <html> element is the root element of the HTML page.
The <head> element is used to define the document's metadata and includes any external CSS or JavaScript files. 
In this case, the <head> section is empty.<br/>
  
Step2:CSS Styling:<br/>
  
The code includes a <style> section that defines the styles for various elements in the UI.
I use universal selector that applies the defined styles to all elements.
The body element is set to occupy 85% of the viewport height and uses CSS Grid to center its contents vertically and horizontally.
The table element is given a fixed width of 1000 pixels and a box shadow effect.
The td and th elements inside the table are styled with padding, a light gray border, and centered text. The th elements have a black background and white text.
Alternating rows of the table have different background colors to improve readability.
  
Step3:UI Components:</br>
  
The h1 element displays the heading Create a UI to show the tickets from the database It has a black background and white text.
The table element is used to create a tabular structure to display the ticket information.
The first row of the table (<tr>) contains the table headers (<th>) for each column: "Ticket Name," "Name," "Description," "Status," and "Reporter."
  
# Flask code
 This code is a Python Flask application that connects to a MySQL database and retrieves data from a table called "fetch_mysql". Let's break it down:


Step1: Importing Required Modules:</br>

The code begins by importing necessary modules: Flask for creating the Flask application, render_template for rendering HTML templates, MySQL for connecting to the MySQL database, and MySQLdb.cursors for using MySQL cursors.
  
Step2:Flask Application Setup:</br>

An instance of the Flask application is created using Flask(__name__) and assigned to the variable app.py
  
Step3:Database Configuration:</br>

The code sets up the configuration for connecting to the MySQL database .</br>
MYSQL_HOST specifies the hostname of the MySQL server (in this case, "localhost").</br>
MYSQL_USER specifies the MySQL username ("root" in this case).</br>
MYSQL_PASSWORD specifies the MySQL password ("Python@ng123" in this case).</br>
MYSQL_DB specifies the name of the database ("flask_html" in this case).</br>
  
  
Step4:MySQL Connection Setup:

An instance of MySQL is created using MySQL(app), which initializes the MySQL extension with the Flask app.
The code defines a route for the root URL ("/") and the "/flask_html" URL, which allows the application to handle GET and POST requests.
a cursor object is created using mysql.connection.cursor(MySQLdb.cursors.DictCursor). This cursor allows executing queries on the MySQL database.
The cursor executes the query "select * from fetch_mysql" to retrieve all records from the "fetch_mysql" table.
The fetched data is stored in the data variable.
Finally, the render_template function is used to render the "index.html" template, passing the data variable to the template for displaying the retrieved data.
  
Step5:Running the Application:</br>

The if __name__ == '__main__': condition ensures that the Flask application is only run if the script is executed directly (not imported as a module).
The app.run() function starts the Flask development server on port 5000 with debugging enabled.  

## ouput be like:-

|Ticket_name|Name|Description|Status|Reporter|
| :-------| :-------|:-------| :-------| :-------|
|JAYAS-1|jaya|None|Done|jaya Srivastaw
|JAYAS-2|jaya|Look this|In progress|jaya srivastaw
|JAYAS-3|jaya|this one|None|jaya Srivastaw
|JAYAS-4|jaya|None|To-do|jaya Srivastaw|

