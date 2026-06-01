    # Part 2: Automated Deployment Risk Assessment
    # Step 2    : Assess the risks of deploying the code using AI

# risk_assessment.py

from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()


client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

deployment_info = """
Files Changed: 65
Database Migration: Yes
Payment Module Modified: Yes
Test Coverage: 58%
"""

prompt = f"""
Assess deployment risk.

Return:
Risk Level
Reason
Recommendation

Data:
{deployment_info}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":prompt}
    ]
)

print(response.choices[0].message.content)