from fastapi import FastAPI
import json

from ai_engine import analyze_code
from jira_service import create_jira_ticket
from github_service import create_fix_pr
from test_runner import run_tests
from repo_manager import clone_repo, apply_fix, cleanup

app = FastAPI()

# 🔗 Your GitHub repo URL
REPO_URL = "https://github.com/vanditmakwana55/ai-qa-agent.git"


# ✅ Clean Gemini response (remove ```json)
def clean_ai_response(text: str):
    text = text.strip()

    if text.startswith("```"):
        text = text.replace("```json", "").replace("```", "")

    return text.strip()


@app.post("/analyze")
def analyze(payload: dict):
    try:
        code = payload["code"]
        file_path = payload["file_path"]

        # 🧠 Step 1: AI analyzes code
        ai_result = analyze_code(code)

        # 🧹 Step 2: Clean AI output
        cleaned = clean_ai_response(ai_result)

        try:
            result = json.loads(cleaned)
        except Exception:
            return {
                "status": "error",
                "message": "Invalid AI response (not JSON)",
                "raw_output": ai_result
            }

        # ❌ No bug found
        if not result.get("bug_found", False):
            return {
                "status": "success",
                "message": "No bug found"
            }

        # 🐞 Step 3: Create Jira Ticket
        issue_key = create_jira_ticket(
            summary=result.get("summary", "AI detected bug"),
            description_data=result
        )

        # 📥 Step 4: Clone Repo
        clone_repo(REPO_URL)

        # 🛠️ Step 5: Apply AI Fix Locally
        apply_fix(file_path, result.get("fix_code", code))

        # 🧪 Step 6: Run Tests on FIXED CODE
        test_result = run_tests("temp_repo")

        if not test_result["success"]:
            cleanup()
            return {
            "status": "failed",
            "message": "Tests failed on AI fix",
            "jira_ticket": issue_key,
            "test_output": test_result["output"],
            "test_error": test_result["error"]
            }

        # 🚀 Step 7: Create PR
        pr_url = create_fix_pr(
            issue_key=issue_key,
            file_path=file_path,
            fixed_code=result.get("fix_code", code)
        )

        # 🧹 Step 8: Cleanup temp repo
        cleanup()

        return {
            "status": "success",
            "message": "Bug fixed and PR created",
            "jira_ticket": issue_key,
            "pr_url": pr_url
        }

    except Exception as e:
        cleanup()
        return {
            "status": "error",
            "message": str(e)
        }