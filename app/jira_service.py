import requests
from requests.auth import HTTPBasicAuth
import os

def create_jira_ticket(summary, description):
    url = f"{os.getenv('JIRA_URL')}/rest/api/3/issue"

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
                            "text": description
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

    # 🔍 Debug print
    print("JIRA RESPONSE:", data)

    if "key" not in data:
        raise Exception(f"Jira Error: {data}")

    return data["key"]