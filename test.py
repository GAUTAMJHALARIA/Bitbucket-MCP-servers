import asyncio
from fastmcp.client import Client

async def test_create_pr(client):
    response = await client.call_tool("create_pr", {
        "createpr": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "source_branch": "demofeature",
            "destination_branch": "main",
            "title": "Add new feature",
            "description": "This PR adds a new feature."
        }
    })
    print("create_pr:", response)

async def test_list_prs(client):
    response = await client.call_tool("list_prs", {
        "listpr": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "state": "OPEN"
        }
    })
    print("list_prs:", response)

async def test_review_pr(client):
    response = await client.call_tool("review_pr", {
        "reviewpr": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1,
            "comment": "Looks good"
        }
    })
    print("review_pr:", response)

async def test_add_task_to_pr_comment(client):
    response = await client.call_tool("add_task_pr_comment", {
        "task": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1,
            "comment_id": 1,
            "task_content": "Task content"
        }
    })
    print("add_task_to_pr_comment:", response)

async def test_get_pull_request_details(client):
    response = await client.call_tool("get_pr_details", {
        "details": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1
        }
    })
    print("get_pull_request_details:", response)

async def test_update_pull_request(client):
    response = await client.call_tool("update_pr", {
        "update": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1,
            "title": "Updated title",
            "description": "Updated description"
        }
    })
    print("update_pull_request:", response)

async def test_get_pr_diff(client):
    response = await client.call_tool("get_pr_diff", {
        "diff": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1
        }
    })
    print("get_pr_diff:", response)

async def test_approve_pull_request(client):
    response = await client.call_tool("approve_pr", {
        "approve": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1
        }
    })
    print("approve_pull_request:", response)

async def test_merge_pull_request(client):
    response = await client.call_tool("merge_pr", {
        "merge": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1,
            "merge_strategy": "merge_commit"
        }
    })
    print("merge_pull_request:", response)

async def test_decline_pull_request(client):
    response = await client.call_tool("decline_pr", {
        "decline": {
            "workspace": "demo145",
            "repo_slug": "demorepo",
            "pr_id": 1
        }
    })
    print("decline_pull_request:", response)

async def main():
    async with Client("http://127.0.0.1:8000/mcp") as client:
         await test_create_pr(client)
        # await test_list_prs(client)
        # await test_review_pr(client)
        # await test_add_task_to_pr_comment(client)
        # await test_get_pull_request_details(client)
        # await test_update_pull_request(client)
        # await test_get_pr_diff(client)
        # await test_approve_pull_request(client)
        # await test_merge_pull_request(client)
        # await test_decline_pull_request(client)

if __name__ == "__main__":
    asyncio.run(main())
