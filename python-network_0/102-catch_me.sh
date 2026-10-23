#!/bin/bash
# Makes a request to a URL that causes the server to respond with "You find me!"
curl -sL -X PUT -d "user_id=98" -H "Origin: HolbertonSchool" "$1"
