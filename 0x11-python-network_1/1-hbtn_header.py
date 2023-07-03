#!/usr/bin/python3
'''
Script that takes in a URL, sends a request to the URL and
    displays the value of the X-Request-Id variable
'''

import urllib.request
from sys import argv

if __name__ == "__main__":
    with urllib.request.urlopen(argv[1]) as response:
        print(dict(response.headers).get("X-Request-Id"))
