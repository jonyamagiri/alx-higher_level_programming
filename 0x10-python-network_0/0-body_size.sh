#!/bin/bash
# takes and sends a request to URL; displays size of the body of the response
curl -sI "$1" | sed -n 's/^Content-Length: *\([0-9]*\)/\1/p'
