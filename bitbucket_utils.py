import os
import requests
from typing import List
from dotenv import load_dotenv
from Models.models import *
load_dotenv()


BITBUCKET_API_URL = "https://api.bitbucket.org/2.0"

def get_auth():
    username = os.getenv("BITBUCKET_USERNAME")
    app_password = os.getenv("BITBUCKET_APP_PASSWORD")
    if not username or not app_password:
        raise EnvironmentError("BITBUCKET_USERNAME or BITBUCKET_APP_PASSWORD not set.")
    return (username, app_password)

def create_pull_request(createpr : CreatePR) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{createpr.workspace}/{createpr.repo_slug}/pullrequests"
    auth = get_auth()
    payload = {
        "title": createpr.title,
        "source": {
            "branch": {
                "name": createpr.source_branch
            }
        },
        "destination": {
            "branch": {
                "name": createpr.destination_branch
            }
        },
        "description":  createpr.description
    }
    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()

def list_pull_requests(listpr : ListPR) -> List[dict]:
    url = f"{BITBUCKET_API_URL}/repositories/{listpr.workspace}/{listpr.repo_slug}/pullrequests"
    auth = get_auth()
    params = {"state": listpr.state}
    response = requests.get(url, auth=auth, params=params)
    response.raise_for_status()
    return response.json().get("values", [])

from Models.models import ReviewPR, AddTaskToPRComment

def review_pull_request(reviewpr: ReviewPR) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{reviewpr.workspace}/{reviewpr.repo_slug}/pullrequests/{reviewpr.pr_id}/comments"
    auth = get_auth()
    payload = {"content": {"raw": reviewpr.comment}}
    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()


def add_task_to_pr_comment(task: AddTaskToPRComment) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{task.workspace}/{task.repo_slug}/pullrequests/{task.pr_id}/comments/{task.comment_id}/tasks"
    auth = get_auth()
    payload = {"content": task.task_content}
    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()



def get_pull_request_details(details: GetPullRequestDetails) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{details.workspace}/{details.repo_slug}/pullrequests/{details.pr_id}"
    auth = get_auth()
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    return response.json()


def update_pull_request(update: UpdatePullRequest) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{update.workspace}/{update.repo_slug}/pullrequests/{update.pr_id}"
    auth = get_auth()
    payload = {}
    if update.title: payload["title"] = update.title
    if update.description: payload["description"] = update.description
    response = requests.put(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()


def get_pull_request_diff(diff: GetPRDiff) -> str:
    url = f"{BITBUCKET_API_URL}/repositories/{diff.workspace}/{diff.repo_slug}/pullrequests/{diff.pr_id}/diff"
    auth = get_auth()
    response = requests.get(url, auth=auth)
    response.raise_for_status()
    return response.text

def approve_pull_request(approve: ApprovePullRequest) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{approve.workspace}/{approve.repo_slug}/pullrequests/{approve.pr_id}/approve"
    auth = get_auth()
    response = requests.post(url, auth=auth)
    response.raise_for_status()
    return response.json()

# def merge_pull_request(merge: MergePullRequest) -> dict:
#     url = f"{BITBUCKET_API_URL}/repositories/{merge.workspace}/{merge.repo_slug}/pullrequests/{merge.pr_id}/merge"
#     auth = get_auth()
#     payload = {"merge_strategy": merge.merge_strategy}  # Options: "merge_commit", "squash", "fast_forward"
#     response = requests.post(url, auth=auth, json=payload)
#     response.raise_for_status()
#     return response.json()

def decline_pull_request(decline: DeclinePullRequest) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{decline.workspace}/{decline.repo_slug}/pullrequests/{decline.pr_id}/decline"
    auth = get_auth()
    response = requests.post(url, auth=auth)
    response.raise_for_status()
    return response.json()

def add_inline_comment(comment: InlineComment) -> dict:
    url = f"{BITBUCKET_API_URL}/repositories/{comment.workspace}/{comment.repo_slug}/pullrequests/{comment.pr_id}/comments"
    auth = get_auth()

    # Build inline payload with only the correct field
    inline_payload = {
        "path": comment.file_path
    }

    if comment.side == "RIGHT":
        inline_payload["to"] = comment.line_number
    elif comment.side == "LEFT":
        inline_payload["from"] = comment.line_number
    else:
        raise ValueError("side must be 'LEFT' or 'RIGHT'")

    payload = {
        "content": {
            "raw": comment.comment_text
        },
        "inline": inline_payload
    }

    response = requests.post(url, auth=auth, json=payload)
    response.raise_for_status()
    return response.json()

