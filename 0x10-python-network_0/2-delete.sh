#!/bin/bash

# Script to send a DELETE request to a URL and display the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a DELETE request to the URL and display the body of the response
curl -s "$1" -X DELETE -w "%{http_code}" | awk '/DELETE/{getline; print}'
