#!/usr/bin/python3
"""Fetches a status URL using urllib with a with statement."""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1] if len(sys.argv) > 1 else 'https://intranet.hbtn.io/status'
    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
