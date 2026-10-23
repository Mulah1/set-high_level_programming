#!/usr/bin/python3
"""Takes in a letter and sends a POST request with q parameter to search API."""
import sys
import requests


if __name__ == '__main__':
    letter = sys.argv[1] if len(sys.argv) > 1 else ""
    payload = {'q': letter}
    response = requests.post('http://0.0.0.0:5000/search_user', data=payload)
    try:
        json_response = response.json()
        if json_response:
            print("[{}] {}".format(json_response.get('id'), json_response.get('name')))
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
