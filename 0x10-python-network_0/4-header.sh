#!/bin/bash
# GET request to a URL with a custom header
curl -s -H "X-School-User-Id: 98" -X GET "$1" | cat
