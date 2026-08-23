#!/usr/bin/python3
"""
Fetches 10 recent commits from a GitHub repository.
"""
import requests
import sys


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"

    response = requests.get(url)
    commits = response.json()

    try:
        for i in range(10):
            sha = commits[i].get('sha')
            author = commits[i].get('commit').get('author').get('name')
            print(f"{sha}: {author}")
    except IndexError:
        pass
