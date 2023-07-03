#!/usr/bin/python3
'''
Script that takes URL and email as arguments and sends
    then sends the email to URL and captures the feedback
'''

from sys import argv
import urllib.request

if __name__ == "__main__":
    URL = argv[1]
    value = {"email": argv[2]}
    data = urllib.parse.urlencode(value).encode("ascii")

    request = urllib.request.Request(URL, data)
    with urllib.request.urlopen(request) as response:
        print(response.read().decode("utf-8"))
