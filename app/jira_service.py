import requests
from requests.auth import HTTPBasicAuth
import os


# 🧠 Convert AI JSON → QA formatted description
def format_jira_description(data):
    issues = "\n".join([f"- {i}" for i in data.get("issues", [])])
    steps = "\n".join([f"{i+1}. {s}" for i, s in enumerate(data.get("steps", []))])

    description_text = f"""
🔍 Issue Summary
{data.get("summary", "N/A")}

------------------------------

❌ Observed Issues
{issues if issues else "N/A"}

------------------------------

🧪 Steps to Reproduce
{steps if steps else "N/A"}

------------------------------

⚠️ Actual Result
{data.get("actual", "N/A")}

------------------------------

✅ Expected Result
{data.get("expected", "N/A")}

------------------------------

🧩 Impact
{data.get("impact", "N/A")}
"""

    return description_text.strip()


# 🚀 Create Jira Ticket
def create_jira_ticket(summary, description_data):
    url = f"{os.getenv('JIRA_URL')}/rest/api/3/issue"

    # 🧾 Format description
    jira_description = format_jira_description(description_data)

    payload = {
        "fields": {
            "project": {"key": os.getenv("JIRA_PROJECT")},
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": jira_description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {"name": "Bug"}
        }
    }

    response = requests.post(
        url,
        json=payload,
        auth=HTTPBasicAuth(
            os.getenv("JIRA_EMAIL"),
            os.getenv("JIRA_API_TOKEN")
        ),
        headers={"Content-Type": "application/json"}
    )

    data = response.json()

    print("JIRA RESPONSE:", data)

    if "key" not in data:
        raise Exception(f"Jira Error: {data}")

    return data["key"]