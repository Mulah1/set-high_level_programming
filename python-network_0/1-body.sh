#!/bin/bash
# Takes in a URL, sends a GET request, and displays the body of the response (following redirects)
curl -sL "$1"
