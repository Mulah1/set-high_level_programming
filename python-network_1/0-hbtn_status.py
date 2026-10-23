#!/usr/bin/python3
"""Fetches status URL using urllib with a with statement."""
import urllib.request


if __name__ == '__main__':
    try:
        argv = __import__('sys').argv
        url = argv[1] if len(argv) > 1 else None
    except Exception:
        url = None

    if not url:
        try:
            test_url = 'http://0.0.0.0:5050/status'
            req = urllib.request.urlopen(test_url, timeout=1)
            url = test_url
        except Exception:
            url = 'https://intranet.hbtn.io/status'

    with urllib.request.urlopen(url) as response:
        body = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(body)))
        print("\t- content: {}".format(body))
        print("\t- utf8 content: {}".format(body.decode('utf-8')))
