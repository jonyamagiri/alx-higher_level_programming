#!/usr/bin/python3
"""
Takes URL and an email, sends a POST request to the URL with the email as a
 parameter, and displays the body of the response (decoded in utf-8)
"""


import sys
import urllib.parse
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1]
    value = {"email": sys.argv[2]}
    data = urllib.parse.urlencode(value).encode('ascii')

    my_request = urllib.request.Request(url, data)
    with urllib.request.urlopen(my_request) as response:
        print(response.read().decode('utf-8'))
