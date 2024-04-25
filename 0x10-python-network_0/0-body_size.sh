#!/bin/bash

# Script to send a request to a URL and display the size of the response body in bytes

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL and display the size of the response body
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
