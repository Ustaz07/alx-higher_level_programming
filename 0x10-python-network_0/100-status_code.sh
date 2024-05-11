#!/usr/bin/python3
"""
Script to list the 10 most recent commits on a given GitHub repository.
"""
import sys
import requests

def list_recent_commits(repo_owner, repo_name):
    """
    Lists the 10 most recent commits on a GitHub repository.
    """
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/commits"
    response = requests.get(url)

    if response.status_code == 200:
        commits = response.json()[:10]
        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    else:
        print("Error:", response.status_code)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: ./script.py <repo_owner> <repo_name>")
        sys.exit(1)

    repo_owner = sys.argv[1]
    repo_name = sys.argv[2]
    list_recent_commits(repo_owner, repo_name)
