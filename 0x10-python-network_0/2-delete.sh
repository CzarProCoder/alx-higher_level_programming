#!/bin/bash
# Bash script that takes a DELETE request to a URL fetched from arguments parsed
curl -sX DELETE "$1"
