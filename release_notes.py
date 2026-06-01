# Part 3: AI Release Note Generation
# Step 3   : Generate release notes using AI based on the code changes and risk assessment

# release_notes.py

from dotenv import load_dotenv
from openai import OpenAI
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

commits = """
Added customer onboarding workflow
Fixed login validation bug
Improved dashboard performance
Added export to excel feature
"""

prompt = f"""
Generate professional release notes.

Commits:
{commits}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":prompt}
    ]
)

print(response.choices[0].message.content)