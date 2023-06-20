# jira_project

## Manage Jira tickets using Python API:
### Task 1:-

Fetch all tickets from Jira API and save that in the database table.

     >> Number
     >> Name
     >> Description
     >> Reporter
     >> Status
     >> Due Date if any

## How I started >>>>>

--At first I made a jira account on Atllasian Jira platform and made few sample tickets to see how the things work, then i spend time on exploring the Jira platform.

--Then I made a API token to attach with my code.

## Move to the coding portion

For the coding part first i saw some videos on youtube how to fetch data from jira ticket one by one.

### Documentation used: 

[Documentation](https://developer.atlassian.com/cloud/jira/platform/rest/v3/api-group-issues/#api-group-issues)


## Commands for Installation

Install Mysql with

```bash
  sudo apt install mysql-server
  sudo mysql_secure_installation
```
Install Jira with

```bash
  pip install jira
```
Install pip
```bash
  sudo apt-get -y install python3-pip
```

## How code is running:-
Step1:- For the first the code requires the jira and mysql-connector-python libraries. You can install them using pip:-
        Install  jira mysql-connector
        
Step2:- Set up the MySQL database. Ensure that you have a MySQL server running and update the code with the appropriate database  
                            (host, username, password, and database name) 

step3:-Set up the Jira connection. Update the Jira server URL and authentication credentials (email and API token).

step4:-Create the MySQL database table. The code will create a table named "FetchIssue_data" in the specified database if it doesn't already exist. The table structure and column definitions are provided in the create_table_query variable.

step5:-This code executes a SQL query to count the number of rows in the "FetchIssue_data" table and stores the result in the variable row_count.

step6:-Fetch issues from the Jira project with the key "JAYAS".

step7:- Check if there are existing issues in the database this is beacuse to ignore duplicate issue insert.

step8:-Insert new records or update existing ones based on the condition.Commit the changes to the database.

step9:-Print a message confirming the successful insertion of data.

step10:- Finall output be like:-

|Number|Name|Description|Reporter|Status|Due_date|Assigne|
| :-------| :-------|:-------| :-------| :-------| :-------|:-------|
|JAYAS-1|ticket-1|test55|Jaya Srivastava|Done|None|jaya Srivastava
|JAYAS-6|for test only-python|just for practice|jaya Srivastava|In Progress|2024-04-19|None|
