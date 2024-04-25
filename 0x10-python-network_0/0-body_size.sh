#!/bin/bash
# Script to display the size of the body of a response from a URL using curl
curl -sI "$1" | grep -i Content-Length | awk '{print $2}'
