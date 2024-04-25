#!/bin/bash
# Script to send a POST request to a URL with parameters and display the body of the response

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a POST request to the URL with parameters and display the body of the response
curl -s "$1" -X POST -d "
email=test@gmail.com&subject=I+will+always+be+here+for+PLD" -w "%{http_code}"
| awk '/POST/{getline; print}'
