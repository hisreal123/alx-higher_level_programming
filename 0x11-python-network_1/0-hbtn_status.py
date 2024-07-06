#!/usr/bin/python3
# A script that feteches https://alx-intranet.hbtn.io/status

import urllib.request

url = "https://alx-intranet.hbtn.io/status"

req = urllib.request.Request(url)

try:
    urllib.request.urlopen(req)
except urllib.error.HTTPError as e:
    print(e.code)
