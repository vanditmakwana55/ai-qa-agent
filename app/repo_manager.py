import os
import shutil
from git import Repo

TEMP_DIR = "temp_repo"

def clone_repo(repo_url, branch="main"):
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)

    Repo.clone_from(repo_url, TEMP_DIR, branch=branch)


def apply_fix(file_path, fixed_code):
    full_path = os.path.join(TEMP_DIR, file_path)

    with open(full_path, "w", encoding="utf-8") as f:
        f.write(fixed_code)


def cleanup():
    if os.path.exists(TEMP_DIR):
        shutil.rmtree(TEMP_DIR)