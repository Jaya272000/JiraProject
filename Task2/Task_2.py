import requests
import json
url = "https://jayasrivastava.atlassian.net/rest/api/3/issue/JAYAS-4/transitions"
headers={
    "Accept": "application/json",
    "Content-Type":"application/json"
}
payload=json.dumps(
    {
        "transition":{
            "id":"31"
        }
    }
)
response=requests.post(url,headers=headers,data=payload,auth=("jaya22@navgurukul.org","ATATT3xFfGF0bDxcm26Rdo_-OJgU5xVIsJj4O8QaaV-DdmJvUengiDTLwEOh_jJ2V-qK1T8FVYJSH9TOIl0i3gzKTRdZ8xj2ed4XWksag4xE12pIFBxuhPXGtHbyRHaoaDqKFZ7yjyvc5jmjTCMgzfh2ACdhu1yIGksOBEAJQUP5oU3N7N5XyKQ=4EA99CFD"))
print(response.text)
print("successful")

