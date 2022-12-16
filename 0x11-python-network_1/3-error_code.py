#!/usr/bin/python3
"""
Takes and sends request to URL; displays body of response (decoded in utf-8)
manages urllib.error.HTTPError exceptions
print: Error code: followed by the HTTP status code
"""


import sys
from urllib import request, error

if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print("Error code: {}".format(e.code))
