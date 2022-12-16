#!/usr/bin/python3
"""
Takes URL and an email address, sends a POST request to given URL with the
 email as a parameter; displays the body of the response
"""


import sys
import requests

if __name__ == "__main__":
    my_data = {'email': sys.argv[2]}
    my_request = requests.post(sys.argv[1], data=my_data)
    print(my_request.text)
