#!/bin/bash
curl -s -i -X OPTIONS "$1" | grep "Allow:" | cut -d' ' -f2-
