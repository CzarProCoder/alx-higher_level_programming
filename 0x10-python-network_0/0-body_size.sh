#!/usr/bin/bash
# Script to take URL, send request to the URL and displays the side of the response
curl -s "$1" | wc -c
