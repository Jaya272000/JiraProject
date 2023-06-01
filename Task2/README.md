## JIRA PROJECT
# TASK-2

--Change the status of the ticket from 'Open' to 'Close' with a comment in Jira using API.


# How I start
-- I already saw the video that was provided by you.
and already complete task 1st so i don't need to make and install anything.

step_1 First i import requests and JSON module for make an HTTP request and for JSON module to work with JSON data.

step_2 I assigning to variable called urn. this variable represents the specific web address URL of API endpoint. 
followed by issue name and transitions.

step_3 I made a header Variable used to specify additional information the request being made to the API.
I used two header 1st headers tell the server that the client expects to receive to response in JSON format.
This header help to ensure communication between client and server by providing clear instruction.

step_4 The payload Variable is used to hold the data.
payloads create using JSON dumps () function.
This function converts a python object in JSON string format.

step_5 At the last establish a connection between the python and Jira server I used basic authentication where provide headers, payloads and username (email associate with Jira software and API Token)

step_6 And print (successful)


# final output:-

I uploaded a screenshot name is final output please check it.

Thank You

