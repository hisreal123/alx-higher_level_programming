#!/usr/bin/python3
# a Python script that takes in a URL, sends a request to the URL and displays the value of the X-Request-Id variable found in the header of the response.


import sys
import urllib.request

if __name__ == "__main__":
    URL = sys.argv[1]  # Get the first argument after the script name
    req = urllib.request.Request(URL)
    with urllib.request.urlopen(req) as response:
        print(dict(response.headers).get("X-Request-Id"))
