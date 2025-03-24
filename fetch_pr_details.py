import requests

from constant import GITHUB_REPO, GITHUB_TOKEN

def fetch_pr(pr_number: int):
    url = f"https://api.github.com/repos/{GITHUB_REPO}/pulls/{pr_number}"
    headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        raise Exception(f"Failed to fetch PR details: {response.status_code}, {response.text}")

    pr_data = response.json()  # Ensure JSON response is parsed into a dictionary
    print("pr_data from github", pr_data)
    # Fetch changed files
    files_url = pr_data.get("url") + "/files"

    print("files_url", files_url)
    files_response = requests.get(files_url, headers=headers).json()
    # print("files_response ==========", files_response)
    # changed_files = [file["filename"] for file in files_response]

    # return {
    #     "title": pr_data.get("title", ""),
    #     "description": pr_data.get("body", ""),
    #     "files_changed": changed_files,
    # }
    return files_response