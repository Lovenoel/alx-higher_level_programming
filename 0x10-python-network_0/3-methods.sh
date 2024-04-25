#!/bin/bash
# Script to display all HTTP methods accepted by a server for a URL using curl
curl -sI -X OPTIONS "$1" | grep -i Allow | awk '{print substr($0, index($0,$2))}'
