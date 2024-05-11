#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the URL with the email as a parameter,
and finally displays the body of the response using the requests package.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {'email': email}
    
    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Raise an error for bad response status
        print("Your email is:", response.text.strip())  # Strip whitespace from the response
    except requests.RequestException as e:
        print(f"Error: {e}")
