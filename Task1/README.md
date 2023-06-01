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
    

Make a database on mysql named "Jira_project" and a table inside it named "Fetched_data".

Write a final pyton code to execute and put my data in that data base.

Final Output Be like :-
|Number|Name|Description|Reporter|Status|Due_date|Assigne|
| :-------| :-------|:-------| :-------| :-------| :-------|:-------|
|JAYAS-1|ticket-1|test55|Jaya Srivastava|Done|None|jaya Srivastava
|JAYAS-6|for test only-python|just for practice|jaya Srivastava|In Progress|2024-04-19|None|
