# test_script.py

import os
import requests

def post_pr_comment(repo_owner, repo_name, pr_number, github_token, comment):
    headers = {
        "Authorization": f"token {github_token}",
        "Accept": "application/vnd.github.v3+json",
    }
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{pr_number}/comments"
    payload = {"body": comment}

    response = requests.post(url, json=payload, headers=headers)
    if response.status_code != 201:
        print(f"Error posting comment: {response.status_code} and message: {response.text}")

if __name__ == "__main__":
    REPO_OWNER = os.environ.get("GITHUB_REPO_OWNER")
    REPO_NAME = os.environ.get("GITHUB_REPO_NAME")
    PR_NUMBER = os.environ.get("GITHUB_PR_NUMBER")
    GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN")

    test_comment = "Hello from the test script! This is a test comment to ensure everything is working correctly."
    post_pr_comment(REPO_OWNER, REPO_NAME, PR_NUMBER, GITHUB_TOKEN, test_comment)
