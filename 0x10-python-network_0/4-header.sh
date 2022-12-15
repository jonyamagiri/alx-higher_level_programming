#!/bin/bash
# takes URL and sends a GET request to it; displays the body of the response
curl -s -H "X-School-User-Id":98 "$1"
