#!/bin/bash
# Takes in a URL, sends a request, and displays the size of the response body in bytes
url="$1"
if [[ ! "$url" =~ ^https?:// ]]; then
    url="http://$url"
fi
curl -s "$url" | wc -c
