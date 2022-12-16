#!/usr/bin/python3
"""
Fetches https://alx-intranet.hbtn.io/status; uses the package requests
"""


import requests

if __name__ == "__main__":
    my_request = requests.get("https://intranet.hbtn.io/status")
    print("Body response:")
    print("\t- type: {}".format(type(my_request.text)))
    print("\t- content: {}".format(my_request.text))
