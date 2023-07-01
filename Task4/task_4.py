# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, redirect, render_template, request, url_for
import jira
from jira import JIRA
from flask import Flask, render_template
import jira
import mysql.connector


# Flask constructor takes the name of
# current module (_name_) as argument.
app = Flask(__name__,template_folder='templates')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success',name = user))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success',name = user))
# The route() function of the Flask class is a decorator,
# which tells the application which URL should call
# the associated function.
# Connect to MySQL database
conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='12345678',
    database='fetch_data'
)

# Create a cursor object to interact with the database
cursor = conn.cursor() 
@app.route("/")
def home():
    return render_template('index.html')
 
@app.route("/educative")
def learn():
    return "Happy Learning at Educative!"

# Route for fetching and storing Jira tickets
@app.route('/check_schema')
def check_schema():


# Connect to MySQL database
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python@ng123",
    database="fetch_data"
)

# Create a database table if it doesn't exist
    cursor = mydb.cursor()
    create_table_query = '''
        CREATE TABLE IF NOT EXISTS new_data1 (
            ID INT AUTO_INCREMENT PRIMARY KEY,
            Number VARCHAR(255),
            Name VARCHAR(255),
            Description TEXT,
            Reporter VARCHAR(255),
            Status VARCHAR(255),
            Due_date DATE,
            Assigne VARCHAR(255)
        )
    '''
    cursor.execute(create_table_query)

    # Check if the table is empty
    cursor.execute("SELECT COUNT(*) FROM new_data1")
    row_count = cursor.fetchone()[0]

    # Connect to Jira
    jira_options = {'server': "https://jayasrivastava.atlassian.net/"}
    jira = JIRA(options=jira_options, basic_auth=("jaya22@navgurukul.org", "ATATT3xFfGF0fLL4BqkKdo_Lp0rTff0vj4dJmluKl9EQX0MCw59eVzRODwCuPV_SeMZD5wUe1K9KN3uq3_2d4HPUfjYXqoObr5NvMH8u8X6jGMx2zoXeF4n3704PTXG20hlfmJozlie5eklIHtheXsCtTTQo4kzHlY4gdGXZ_AolT4Qn4S3JCSk=96502321"))

    # Fetch issues from Jira
    issues = jira.search_issues(jql_str='project = JAYAS')

    # Create a set to store existing issue numbers in the database
    existing_issue_numbers = set()

    if row_count > 0:
        # Fetch existing issue numbers from the database
        cursor.execute("SELECT Number FROM new_data1")
        existing_issues = cursor.fetchall()
        existing_issue_numbers = {issue[0] for issue in existing_issues}

    # Insert new records into the database and update existing ones
    for singleIssue in issues:
        Number = singleIssue.key
        Name = singleIssue.fields.summary
        Description = singleIssue.fields.description
        Reporter = singleIssue.fields.reporter.displayName
        Status = singleIssue.fields.status.name
        Due_date = singleIssue.fields.duedate
        Assignee = singleIssue.fields.assignee.displayName if singleIssue.fields.assignee else None

        if Number in existing_issue_numbers:
            # Update existing record
            query = "UPDATE new_data1 SET Name = %s, Description = %s, Reporter = %s, Status = %s, Due_date = %s, Assigne = %s WHERE Number = %s"
            values = (Name, Description, Reporter, Status, Due_date, Assignee, Number)
        else:
            # Insert new record
            query = "INSERT INTO new_data1 (Number, Name, Description, Reporter, Status, Due_date, Assigne) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            values = (Number, Name, Description, Reporter, Status, Due_date, Assignee)

        cursor.execute(query, values)
        mydb.commit()
        return 'Data inserted into the database.'
print("Data inserted into the database.")
# main driver function
if __name__ == '_main_':

	# run() method of Flask class runs the application
	# on the local development server.
   app.run(debug=True)
	# app.run()