import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ✅ Initialize the client safely for Azure and local both
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_cr_description(description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Change Management expert validating CRs."},
            {"role": "user", "content": f"Validate this Change Request: {description}"}
        ]
    )
    return {"validation": response.choices[0].message.content.strip()}

def assess_risk(description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a Change Risk Assessment Assistant."},
            {"role": "user", "content": f"Assess the risk for this CR: {description}. Respond with one of: Low, Medium, or High, and explain why."}
        ]
    )
    content = response.choices[0].message.content.strip()
    if ":" in content:
        risk, reason = content.split(":", 1)
        return risk.strip(), reason.strip()
    return "Unknown", content

def generate_suggestions(description):
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a CR Improvement Advisor."},
            {"role": "user", "content": f"Suggest improvements for this Change Request: {description}"}
        ]
    )
    return [s.strip() for s in response.choices[0].message.content.strip().split('\n') if s.strip()]
