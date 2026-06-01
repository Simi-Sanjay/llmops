# Part 4: AI Log Analysis
# Step 4 - Analyze the logs using AI techniques to identify patterns and insights.

# log_analyzer.py


from openai import OpenAI
import os
from dotenv import load_dotenv
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

logs = """
ERROR Connection Timeout
ERROR Connection Timeout
ERROR Connection Timeout

WARNING Pool Size Exceeded

ERROR Database Connection Failed
"""

prompt = f"""
Analyze logs.

Provide:
1. Root Cause
2. Severity
3. Recommendation

Logs:
{logs}
"""

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role":"user","content":prompt}
    ]
)

print(response.choices[0].message.content)

