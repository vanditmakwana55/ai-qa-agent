import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

def analyze_code(code: str):
    prompt = f"""
    Analyze the following Python code and identify bugs.

    Return ONLY valid JSON (no markdown).

    Format:
    {{
    "bug_found": true,
    "summary": "Short title of bug",
    "issues": [
        "Issue 1",
        "Issue 2"
    ],
    "steps": [
        "Step 1",
        "Step 2"
    ],
    "expected": "Expected behavior",
    "actual": "Actual behavior",
    "impact": "Impact of bug",
    "fix_code": "fixed code"
    }}

    Code:
    {code}
    """

    response = model.generate_content(prompt)
    return response.text