# review_code.py
# Part 1: AI Code Review
# Step 1: Read the code from a file


from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

with open("sample.py","r") as f:
    code = f.read()

prompt = f"""
Review this code.

Identify:
1. Bugs
2. Security issues
3. Performance issues
4. Code smells

Code:
{code}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":prompt}
    ]
)

print(response.choices[0].message.content)