#!/bin/bash
# a POST request with parameters to a URL
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1" | cat

