#!/bin/bash
# send a DELETE request to a URL, display the body of the response using curl
curl -s -X DELETE "$1" | cat

