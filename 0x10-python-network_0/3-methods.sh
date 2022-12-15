#!/bin/bash
# takes in a URL and displays all HTTP methods the server will accept
response=$(curl -sI "$1" | grep 'Allow:') && echo "$response" | cut -f2- -d' '
