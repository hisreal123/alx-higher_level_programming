#!/bin/bash
#a Bash script that makes a request to 0.0.0.0:5000/catch_me that causes the server to respond with a message containing You got me!, in the body of the response.
curl -sL -X PUT -H "Origin: School" -d "user_id=89" 0.0.0.0:5000/catch_me
