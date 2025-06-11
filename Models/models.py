from pydantic import BaseModel,Field
from typing import Literal

class BaseRequest(BaseModel):
    workspace :  str = Field(..., description="Workspace name")
    repo_slug : str = Field(..., description="Repository name")
class PRRequest(BaseRequest):
    pr_id: int = Field(..., description="Pull Request ID", gt=0)

class CreatePR(BaseRequest):
    title : str = Field(..., description="Pull Request Title")
    source_branch : str = Field(..., description="Source branch name")
    destination_branch : str = Field(default="main", description="Destination branch name")
    description : str = Field(default="", description="Pull request description")
    
class ListPR(BaseRequest):
    state : str = Field(default="OPEN", description="Pull request State")

class ReviewPR(BaseRequest):
    pr_id: int = Field(..., description="Pull Request ID")
    comment: str = Field(..., description="Review comment")


class AddTaskToPRComment(BaseRequest):
    pr_id: int = Field(..., description="Pull Request ID")
    comment_id: int = Field(..., description="Comment ID")
    task_content: str = Field(..., description="Task content")

class GetPullRequestDetails(BaseRequest):
    pr_id: int = Field(..., description="Pull Request ID")

class UpdatePullRequest(BaseRequest):
    pr_id: int = Field(..., description="Pull Request ID")
    title: str = Field(None, description="Pull Request Title")
    description: str = Field(None, description="Pull Request Description")



GetPullRequestDetails = PRRequest
GetPRDiff = PRRequest
ApprovePullRequest = PRRequest
DeclinePullRequest = PRRequest

    
class InlineComment(PRRequest):
    file_path: str = Field(..., description="File path for the comment")
    line_number: int = Field(..., description="Line number", gt=0)
    comment_text: str = Field(..., description="Comment text", min_length=1)
    side: Literal["LEFT", "RIGHT"] = Field(default="RIGHT", description="Comment side - LEFT (old) or RIGHT (new)")
    

    
    