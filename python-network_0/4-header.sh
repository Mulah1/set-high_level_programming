#!/bin/bash
# Takes in a URL, sends a GET request with a custom header variable, and displays the body
curl -s -H "X-School-User-Id: 98" "$1"
