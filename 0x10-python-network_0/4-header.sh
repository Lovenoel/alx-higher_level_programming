#!/bin/bash

"""Script to send a GET request to a URL with a custom header and display 
the body of the response
"""

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a GET request to the URL with a custom header and display the body of the response
curl -s "$1" -X GET -H "X-School-User-Id: 98" -w "%{http_code}" | awk '/98/{getline; print}'
