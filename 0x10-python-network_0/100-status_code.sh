#!/bin/bash
# This script sends a request to a URL passed as an argument and displays only the status code of the response

# Send a HEAD request to the specified URL and output only the HTTP status code
curl -s -o /dev/null -w "%{http_code}" "$1"
