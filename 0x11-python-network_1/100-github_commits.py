#!/usr/bin/python3
"""
Python script that lists 10 commits (from the most recent to oldest)
of the repository “rails” by the user “rails”
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print(f"Error: {response.status_code}")
