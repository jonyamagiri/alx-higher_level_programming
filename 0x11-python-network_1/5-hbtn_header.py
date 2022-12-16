#!/usr/bin/python3
"""
Takes and sends request to URL; displays the value of the variable
 X-Request-Id in the response header using the packages requests and sys
"""


import sys
import requests

if __name__ == "__main__":
    my_request = requests.get(sys.argv[1])
    print(my_request.headers.get('X-Request-Id'))
