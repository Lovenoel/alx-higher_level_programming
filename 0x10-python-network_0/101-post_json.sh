#!/bin/bash
# a JSON POST request to a URL with the contents of a file
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
