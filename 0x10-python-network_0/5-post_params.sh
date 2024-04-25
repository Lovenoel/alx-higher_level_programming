#!/bin/bash
# Send a POST request to the provided URL with email and subject parameters, then display the response body
curl -s -X POST "$1" -d "email=test@gmail.com" \
	-d "subject=I will always be here for PLD"
