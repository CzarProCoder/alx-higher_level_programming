#!/usr/bin/bash
# Script to take URL, send request to the URL an
#	displays the side of the response

curl -s "$1" | wc -c
