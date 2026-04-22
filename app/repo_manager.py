import os
import shutil
import stat
import time
from git import Repo

TEMP_DIR = "temp_repo"


# 🔧 Fix for Windows read-only file deletion
def handle_remove_readonly(func, path, exc):
    try:
        os.chmod(path, stat.S_IWRITE)
        func(path)
    except Exception as e:
        print(f"Force delete failed for {path}: {e}")


# 🧹 Safe cleanup with retry (prevents WinError 5)
def cleanup():
    if os.path.exists(TEMP_DIR):
        for i in range(3):  # retry 3 times
            try:
                shutil.rmtree(TEMP_DIR, onerror=handle_remove_readonly)
                print("✅ Temp repo cleaned")
                break
            except Exception as e:
                print(f"⚠️ Cleanup retry {i+1}: {e}")
                time.sleep(1)


# 📥 Clone repo safely
def clone_repo(repo_url, branch="main"):
    cleanup()  # always clean before cloning

    try:
        Repo.clone_from(repo_url, TEMP_DIR, branch=branch)
        print("✅ Repo cloned successfully")
    except Exception as e:
        raise Exception(f"❌ Clone failed: {e}")


# 🛠️ Apply AI-generated fix to file
def apply_fix(file_path, fixed_code):
    full_path = os.path.join(TEMP_DIR, file_path)

    if not os.path.exists(full_path):
        raise Exception(f"❌ File not found in repo: {file_path}")

    try:
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(fixed_code)
        print(f"✅ Fix applied to {file_path}")
    except Exception as e:
        raise Exception(f"❌ Failed to write fix: {e}")