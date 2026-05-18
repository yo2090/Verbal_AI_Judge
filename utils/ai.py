import os
import requests
from dotenv import load_dotenv

load_dotenv()

OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

PROMPT = '''
You are a senior verbal marketing strategist.

Analyze this homepage copy.

Evaluate:
- clarity
- positioning
- customer focus
- CTA quality
- emotional resonance

Return:
- overall score
- biggest problem
- biggest opportunity
- strengths
- weaknesses
- rewrite suggestions
- improved homepage headline

Keep the report concise and easy to understand.
'''

def generate_report(website_text):
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENROUTER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "deepseek/deepseek-chat-v3-0324:free",
            "messages": [
                {
                    "role": "system",
                    "content": PROMPT
                },
                {
                    "role": "user",
                    "content": website_text
                }
            ]
        },
        timeout=60
    )

    data = response.json()

    return data["choices"][0]["message"]["content"]
