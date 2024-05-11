#!/bin/bash
# Sends a HEAD request to the specified URL and displays only the HTTP status code.
# Usage: ./get_status_code.sh <URL>

if [ $# -ne 1 ]; then echo "Usage: $0 <URL>"; exit 1; fi
curl -s -o /dev/null -w "%{http_code}" "$1"
