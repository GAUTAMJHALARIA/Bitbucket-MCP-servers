from fastmcp import FastMCP
from bitbucket_utils import *
from Models.models import *
mcp = FastMCP("Bitbucket PR Automation Server")

@mcp.tool()
def create_pr(createpr: CreatePR) -> dict:
    """
    Create a new pull request in Bitbucket.
    """
    return create_pull_request(createpr)

@mcp.tool()
def list_prs(listpr : ListPR) -> list:
    """
    List pull requests for a Bitbucket repository.
    """
    return list_pull_requests(listpr)

@mcp.tool()
def review_pr(reviewpr: ReviewPR) -> dict:
    """
    Post a review comment on a Bitbucket pull request.
    """
    return review_pull_request(reviewpr)

@mcp.tool()
def add_task_pr_comment(task: AddTaskToPRComment) -> dict:
    """
    Add a task  on a Bitbucket pull request comment.
    """
    return add_task_to_pr_comment(task)


# existing imports and code above unchanged
@mcp.tool()
def get_pr_details(details: GetPullRequestDetails) -> dict:
    """
    Get details of a Bitbucket pull request.
    """
    return get_pull_request_details(details)

@mcp.tool()
def update_pr(update: UpdatePullRequest) -> dict:
    """
    Update a Bitbucket pull request.
    """
    return update_pull_request(update)

@mcp.tool()
def get_pr_diff(diff: GetPRDiff) -> str:
    """
    Get the diff of a Bitbucket pull request.
    """
    return get_pull_request_diff(diff)

@mcp.tool()
def approve_pr(approve: ApprovePullRequest) -> dict:
    """
    Approve a Bitbucket pull request.
    """
    return approve_pull_request(approve)

# @mcp.tool()
# def merge_pr(merge: MergePullRequest) -> dict:
#     """
#     Merge a Bitbucket pull request.
#     """
#     return merge_pull_request(merge)

@mcp.tool()
def decline_pr(decline: DeclinePullRequest) -> dict:
    """
    Decline a Bitbucket pull request.
    """
    return decline_pull_request(decline)

if __name__ == "__main__":
     mcp.settings.port = 3005
     mcp.run(transport="sse")
