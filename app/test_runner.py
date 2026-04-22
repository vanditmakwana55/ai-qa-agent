import subprocess
import sys
import os

def run_tests(repo_path):
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        capture_output=True,
        text=True,
        cwd=repo_path
    )

    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)

    return result.returncode == 0