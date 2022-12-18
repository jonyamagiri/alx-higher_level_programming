#!/usr/bin/python3
"""
Lists 10 most recent commits of a given repository and user with the GitHub API
Print all commits by: `<sha>: <author name>` (one by line)
"""


if __name__ == "__main__":
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    list_commits = r.json()
    for commit in list_commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
