#!/bin/bash
# Takes in a URL and displays the HTTPS methods that the server will take
curl -sI "$1" | grep 'Allow:' | cut -f2- -d' '
