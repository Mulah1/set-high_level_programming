#!/usr/bin/python3
"""Lists 10 commits of a repository by a user using GitHub API."""
import sys
import requests


if __name__ == '__main__':
    repo = sys.argv[1]
    owner = sys.argv[2]
    url = 'https://api.github.com/repos/{}/{}/commits'.format(owner, repo)
    response = requests.get(url)
    try:
        commits = response.json()
        for commit in commits[:10]:
            sha = commit.get('sha')
            author_name = commit.get('commit').get('author').get('name')
            print("{}: {}".format(sha, author_name))
    except Exception:
        pass
