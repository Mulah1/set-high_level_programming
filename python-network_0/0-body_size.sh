#!/bin/bash
<<<<<<< HEAD
curl -s "$1" | wc -c
=======
# Takes in a URL, sends a request, and displays the size of the body of the response in bytes
curl -s -o /dev/null -w '%{size_download}\n' "$1"
>>>>>>> 9988635cbd3733f38903f2296d384ff89c08f3c1
