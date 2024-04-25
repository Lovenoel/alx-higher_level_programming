#!/bin/bash

# Script to display all HTTP methods the server will accept for a given URL

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Display all HTTP methods accepted by the server for the given URL
curl -sI "$1" | awk '/Allow/{print substr($0, index($0,$2))}'
