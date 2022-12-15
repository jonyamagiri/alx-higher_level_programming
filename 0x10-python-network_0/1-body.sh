#!/bin/bash
# takes and sends a GET to URL; displays only body of a 200 status code response
curl -sL "$1" | grep -E "^< HTTP/2 200"
