#!/bin/bash
# Displays only the status code of the response without using pipes or redirection
curl -s -o /dev/null -w "%{http_code}" "$1"
