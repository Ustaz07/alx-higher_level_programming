#!/usr/bin/python3
"""
Script that takes in a URL and an email address,
sends a POST request to the URL with the email as a parameter,
and finally displays the body of the response using the requests package.
"""
import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    
    # Extract email from response body
    email_response = response.text.split("Email: ")[1].strip()
    print("Your email is:", email_response)
