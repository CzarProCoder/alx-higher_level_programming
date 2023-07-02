#!/bin/bash
# Takes a URL as argument and sends a GET request with a header variable
curl -sH "X-School-User-Id: 98" "$1"
