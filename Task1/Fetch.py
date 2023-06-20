from jira import JIRA
import mysql.connector

# Connect to MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Python@ng123",
    database="jira_project"
)

# Create a database table if it doesn't exist
cursor = mydb.cursor()
create_table_query = '''
    CREATE TABLE IF NOT EXISTS FetchIssue_data (
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
cursor.execute("SELECT COUNT(*) FROM FetchIssue_data ")
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
    cursor.execute("SELECT Number FROM FetchIssue_data")
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
        query = "UPDATE FetchIssue_data SET Name = %s, Description = %s, Reporter = %s, Status = %s, Due_date = %s, Assigne = %s WHERE Number = %s"
        values = (Name, Description, Reporter, Status, Due_date, Assignee, Number)
    else:
        # Insert new record
        query = "INSERT INTO FetchIssue_data (Number, Name, Description, Reporter, Status, Due_date, Assigne) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        values = (Number, Name, Description, Reporter, Status, Due_date, Assignee)

    cursor.execute(query, values)
    mydb.commit()

print("Data inserted into the database.")
