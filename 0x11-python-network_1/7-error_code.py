#!/usr/bin/python3
"""
Takes and sends request to URL; displays body of response
If HTTP status code is >= 400, print: Error code: followed by HTTP status code
"""


import sys
import requests

if __name__ == "__main__":
    my_req = requests.get(sys.argv[1])
    if my_req.status_code >= 400:
        print("Error code: {}".format(my_req.status_code))
    else:
        print(my_req.text)
