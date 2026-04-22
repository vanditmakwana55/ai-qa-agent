import subprocess
import sys

def run_tests(repo_path):
    try:
        result = subprocess.run(
            [sys.executable, "-m", "pytest", "tests"],
            capture_output=True,
            text=True,
            cwd=repo_path,
            timeout=15   # 🔥 ADD THIS
        )

        return {
            "success": result.returncode == 0,
            "output": result.stdout,
            "error": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {
            "success": False,
            "output": "",
            "error": "Test execution timed out"
        }