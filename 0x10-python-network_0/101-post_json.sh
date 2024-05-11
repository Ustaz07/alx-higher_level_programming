#!/bin/bash
# Sends a JSON POST request to a URL with the contents of a file as the body
# Usage: ./101-post_json.sh <URL> <file>

# Check if the correct number of arguments are provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <URL> <file>"
    exit 1
fi

# Check if the file exists and is readable
if [ ! -r "$2" ]; then
    echo "File not found or not readable: $2"
    exit 1
fi

# Send a POST request with the contents of the file as JSON data
response=$(curl -s -X POST -H "Content-Type: application/json" -d @"$2" "$1")

# Check if the response contains "Valid JSON"
if grep -q "Valid JSON" <<< "$response"; then
    echo "Valid JSON"
else
    echo "Not a valid JSON"
fi
