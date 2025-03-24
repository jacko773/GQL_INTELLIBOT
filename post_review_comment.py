def post_github_comment(pr_number, comment):
    gh = login(token=GITHUB_TOKEN)
    repo = gh.repository(*GITHUB_REPO.split('/'))
    pr = repo.pull_request(pr_number)
    pr.create_comment(comment)