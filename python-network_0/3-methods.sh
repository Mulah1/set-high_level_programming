#!/bin/bash
# Displays all HTTP methods the server will accept
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
