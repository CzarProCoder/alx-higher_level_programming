#!/usr/bin/python3
'''
Script that sends a request to a URL and displays the body of the reponse
It also handles HTTPError
'''

from sys import argv
from urllib import request, error

if __name__ == "__main__":
    url = argv[1]

    try:
        with request.urlopen(url) as response:
            print(response.read().decode("utf-8"))
    except error.HTTPError as e:
        print(f"Error code: {e.code}")
