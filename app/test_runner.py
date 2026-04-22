import subprocess
import sys

def run_tests(repo_path):
    result = subprocess.run(
        [sys.executable, "-m", "pytest"],
        capture_output=True,
        text=True,
        cwd=repo_path
    )

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)
    print("RETURN CODE:", result.returncode)

    return result.returncode == 0