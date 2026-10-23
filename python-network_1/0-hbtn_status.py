#!/usr/bin/python3
"""Fetches a URL (defaulting to intranet.hbtn.io/status) using urllib"""
import sys
import urllib.request

if __name__ == "__main__":
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://intranet.hbtn.io/status'
    
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print(f"\t- type: {type(body)}")
        print(f"\t- content: {body}")
        print(f"\t- utf8 content: {body.decode('utf-8')}")
