from jira import JIRA
from jira import JIRA
import mysql
import mysql.connector
mydb = mysql.connector.connect(
              host="localhost",
              user="root",
              password="Python@ng123",
              database="Jira_project")
jiraoptions = {'server': "https://jayasrivastava.atlassian.net/"}
jira = JIRA(options = jiraoptions, basic_auth = ("jaya22@navgurukul.org","ATATT3xFfGF0fLL4BqkKdo_Lp0rTff0vj4dJmluKl9EQX0MCw59eVzRODwCuPV_SeMZD5wUe1K9KN3uq3_2d4HPUfjYXqoObr5NvMH8u8X6jGMx2zoXeF4n3704PTXG20hlfmJozlie5eklIHtheXsCtTTQo4kzHlY4gdGXZ_AolT4Qn4S3JCSk"))
cursor=mydb.cursor()
for singleIssue in jira.search_issues(jql_str='project = JAYAS'):
    Number=singleIssue.key
    # print(Number)
    Name=singleIssue.fields.summary
    Description=singleIssue.fields.description
    Reporter=singleIssue.fields.reporter.displayName
    Status=singleIssue.fields.status
    Due_Date=singleIssue.fields.duedate
    Assigne=singleIssue.fields.assignee
    query="insert into Fetched_data (Number,Name,Reporter,Status,Due_Date,Description,Assigne) values ('{}','{}','{}','{}','{}','{}','{}')".format(Number,Name,Reporter,Status,Due_Date,Description,Assigne)
    cursor.execute(query)
    mydb.commit()
print("data_inserted")