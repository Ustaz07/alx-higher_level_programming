#!/usr/bin/python3
"""
Script that sends a POST request to a
specified URL with an email as a parameter
and displays the body of the response.
Usage: ./6-post_email.py <URL> <email>
  - Displays the body of the response.
"""

import sys
import requests


def main():
    if len(sys.argv) != 3:
        print("Usage: ./6-post_email.py <URL> <email>")
        sys.exit(1)

    url = sys.argv[1]
    email = sys.argv[2]

    payload = {"email": email}

    try:
        response = requests.post(url, data=payload)
        response.raise_for_status()  # Bad response status
        print(response.text)
    except requests.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
