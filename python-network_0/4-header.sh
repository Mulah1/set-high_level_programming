#!/bin/bash
# Sends a GET request with the header variable X-School-User-Id: 98
curl -s -H "X-School-User-Id: 98" "$1"
