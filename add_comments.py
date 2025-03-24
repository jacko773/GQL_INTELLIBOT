import requests

from constant import GITHUB_REPO, GITHUB_TOKEN

headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

# Add Multiple Inline Comments
def add_multiple_comments(comments, PR_NUMBER: int):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls/{PR_NUMBER}/comments"
    responses = []
    
    for comment in comments:
        data = {
            "body": comment["review_comment"],
            "commit_id": "24e999f997ea1178022a63ebdd5010fa7f4614e8",
            "path": "javaquiz3/schema.gql",
            "position": comment["line_number"],
        }
        response = requests.post(url, json=data, headers=headers)
        responses.append(response.json())

    print("responses from github comments", responses)
    return responses