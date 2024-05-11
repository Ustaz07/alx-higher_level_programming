#!/usr/bin/python3
"""
Lists the 10 most recent commits on a given GitHub repository.
"""

import sys
import requests


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 script.py <repository_name> <owner_name>")
        sys.exit(1)

    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad response status
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get("sha")
            author_name = commit.get("commit").get("author").get("name")
            print(f"{sha}: {author_name}")
    except requests.RequestException as e:
        print(f"Error: {e}")
    except KeyError:
        print("Error: Malformed data from GitHub API")
    except IndexError:
        print("Error: Not enough commits available")


if __name__ == "__main__":
    main()
