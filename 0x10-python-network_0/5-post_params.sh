#!/bin/bash
# takes and sends a POST request to it; displays the body of the response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
