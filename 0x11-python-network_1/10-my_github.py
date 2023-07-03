#!/usr/bin/python3
'''
Script that takes Github credentials (username and password)
    and uses Github API to display id
Uses Basic Authentication with a personal access token as password
    to access to user information (only read:user permission is needed)
Args:
    1st Argument (Github Username)
    2nd Argument (Github Password) -> Personal access token
'''

import requests
from sys import argv
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r = requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))
