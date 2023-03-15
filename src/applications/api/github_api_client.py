import requests


class GitHupApiClient: 

    def search_repo(repo_name):
        r = requests.get("URL")

        return r.body.json()
