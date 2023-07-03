#!/usr/bin/python3
'''
Script that fetches a url and displays the error code if greater than 400
'''

from sys import argv
import requests

if __name__ == "__main__":
    url = argv[1]
    r = requests.get(url)
    if r.status_code >= 400:
        print(f"Error code: {r.status_code}")
    else:
        print(r.text)
