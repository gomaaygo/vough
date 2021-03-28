# Imports
import requests
import json


def get_public_members(login):
    """
        Function that requests the github api and defines the
        number of members of an organization.
    """
    response = requests.get(
        f'https://api.github.com/orgs/{login}/public_members')
    if response.status_code == 200:
         public_members = response.json()
         return len(public_members)
    else:
        return response.status_code  


def get_public_repos(login):
    """
       Function that requests the github api and defines the
       number of repositories for an organization
    """
    response = requests.get(
        f'https://api.github.com/orgs/{login}/repos')

    if response.status_code == 200:
        public_repos = response.json()
        return len(public_repos)
    else:
        return response.status_code  


def get_score(login):
    """
        Function that calculates the organization's score
        number.
    """
    members = get_public_members(login)
    repos = get_public_repos(login)

    score = members + repos

    return score
