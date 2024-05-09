#!/bin/bash

# Send a request to the provided URL, then display the size of the response body in bytes

# Use curl to fetch the URL and store the response body in a variable
response=$(curl -sI "$1" | grep -i "Content-Length" | awk '{print $2}')

# Display the size of the response body
echo "$response"
