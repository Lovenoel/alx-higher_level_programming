#!/bin/bash
# Script to display the body of a response from a URL using curl
curl -s -X GET "$1" | cat
