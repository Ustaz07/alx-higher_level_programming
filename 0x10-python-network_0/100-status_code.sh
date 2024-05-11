#!/bin/bash
# Sends a HEAD request to the specified URL and displays only the HTTP status code.
# Usage: ./get_status_code.sh <URL>

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send a HEAD request to the specified URL and output only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
