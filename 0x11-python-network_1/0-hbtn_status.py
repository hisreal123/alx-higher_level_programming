#!/usr/bin/python3
# A script that feteches https://alx-intranet.hbtn.io/status

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

if __name__ == "__main__":
    req = urllib.request.Request(url)
    with urllib.request.urlopen(req) as res:
        body = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode("utf-8")))
