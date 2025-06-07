from pydantic import BaseModel,Field

class CreatePR(BaseModel):
    workspace :  str = Field(..., description="Workspace name")
    repo_slug : str = Field(..., description="Repository name")
    title : str = Field(..., description="Pull Request Title")
    source_branch : str = Field(..., description="Source branch name")
    destination_branch : str = Field(default="main", description="Destination branch name")
    description : str = Field(default="", description="Pull request description")
    
class ListPR(BaseModel):
    workspace :  str = Field(..., description="Workspace name")
    repo_slug : str = Field(..., description="Repository name")
    state : str = Field(default="OPEN", description="Pull request State")

class ReviewPR(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")
    comment: str = Field(..., description="Review comment")


class AddTaskToPRComment(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")
    comment_id: int = Field(..., description="Comment ID")
    task_content: str = Field(..., description="Task content")

class GetPullRequestDetails(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")

class UpdatePullRequest(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")
    title: str = Field(None, description="Pull Request Title")
    description: str = Field(None, description="Pull Request Description")

class GetPRDiff(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")

class ApprovePullRequest(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")

class MergePullRequest(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")
    merge_strategy: str = Field("merge_commit", description="Merge strategy")

class DeclinePullRequest(BaseModel):
    workspace: str = Field(..., description="Workspace name")
    repo_slug: str = Field(..., description="Repository name")
    pr_id: int = Field(..., description="Pull Request ID")
    