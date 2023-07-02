#!/bin/bash
# Send a post request to server via the URL passed as argument
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
