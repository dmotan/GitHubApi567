# -*- coding: utf-8 -*-
"""
Created on Mar 6 2021

The primary goal of this file is to demonstrate a simple python program to
develop with the perspective of the tester in mind.

@author: Diaeddin Motan
"""

import requests
import json
import sys
from typing import Dict

def getGithubData(githubUserId: str):

    req1 = requests.get(f'https://api.github.com/users/{githubUserId}')
    github_id = json.loads(req1.text)
    # Check whether github id exists or not
    if 'message' in github_id:
        return f'{githubUserId} does not exists'
    # Github id exists
    else:
        req2 = requests.get(f'https://api.github.com/users/{githubUserId}/repos')
        repos = json.loads(req2.text)
        # Check if there are no repos
        if len(repos) == 0:
            return 'No repos'
        # There are repos
        else:
            data: Dict[str, int] = dict()
            for repo in repos:
                repo_name = repo['name']
                req3 = requests.get(f'https://api.github.com/repos/{githubUserId}/{repo_name}/commits')
                commits = json.loads(req3.text)
                data[repo['name']] = len(commits)

            # print the result
            for repo, commits in data.items():
                print(f'Repo: {repo} Number of commits: {commits}')
            return data
