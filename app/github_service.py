from github import Github
import os

g = Github(os.getenv("GITHUB_TOKEN"))
repo = g.get_repo(os.getenv("GITHUB_REPO"))

def create_fix_pr(issue_key, file_path, fixed_code):

    branch = f"fix-{issue_key}"

    source = repo.get_branch("main")
    repo.create_git_ref(ref=f"refs/heads/{branch}", sha=source.commit.sha)

    contents = repo.get_contents(file_path, ref="main")

    repo.update_file(
        path=file_path,
        message=f"{issue_key} AI Fix",
        content=fixed_code,
        sha=contents.sha,
        branch=branch
    )

    pr = repo.create_pull(
        title=f"{issue_key} Auto Fix",
        body="AI generated fix using Gemini",
        head=branch,
        base="main"
    )

    return pr.html_url