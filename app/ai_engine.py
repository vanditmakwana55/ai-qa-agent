import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-flash-latest")

def analyze_code(code: str):
    prompt = f"""
    Analyze the following code.

    1. Find bugs
    2. Suggest fix
    3. Return STRICT JSON:

    {{
        "bug_found": true/false,
        "summary": "...",
        "description": "...",
        "fix_code": "..."
    }}

    Code:
    {code}
    """

    response = model.generate_content(prompt)
    return response.text