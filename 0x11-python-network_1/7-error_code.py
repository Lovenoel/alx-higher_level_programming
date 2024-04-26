#!/usr/bin/python3
""" takes in a URL, sends a request to the URL and displays the body of the
response.
"""
import requests
import sys

url = sys.argv[1]

try:
    response = requests.get(url)
    response.raise_for_status()
    print(response.text)
except requests.HTTPError as e:
    print("Error code:", e.response.status_code)
