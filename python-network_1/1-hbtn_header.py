#!/usr/bin/python3
"""Takes in a URL, sends a request, and displays the X-Request-Id header value."""
import sys
import urllib.request


if __name__ == '__main__':
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        header_value = response.headers.get('X-Request-Id')
        print(header_value)
