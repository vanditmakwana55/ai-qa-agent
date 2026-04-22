import subprocess
import sys

def run_tests(repo_path):
    result = subprocess.run(
        [sys.executable, "-m", "pytest", "tests"],
        capture_output=True,
        text=True,
        cwd=repo_path
    )

    print("STDOUT:\n", result.stdout)
    print("STDERR:\n", result.stderr)

    return {
        "success": result.returncode == 0,
        "output": result.stdout,
        "error": result.stderr
    }