import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def safe_parse(response_text):
    """Safely parse model output to JSON."""
    try:
        return json.loads(response_text)
    except json.JSONDecodeError:
        return {"error": "Invalid JSON from model", "raw": response_text}

def validate_cr_description(description):
    """Validate a change request description for completeness."""
    prompt = f"""
    You are a Change Management validator.
    Analyze this change request description and return ONLY a JSON response in this format:
    {{
        "summary": "Short summary of what the CR describes.",
        "missing_fields": ["List any missing details"],
        "issues": ["List any unclear points"],
        "quality": "Good / Average / Poor"
    }}

    Description:
    {description}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    content = response.choices[0].message.content.strip()
    return safe_parse(content)

def assess_risk(description, environment="PROD"):
    """Assess the risk level of the CR."""
    prompt = f"""
    You are a Change Risk Assessor.
    Read the CR description and environment and return ONLY a JSON object like:
    {{
        "score": "Low / Medium / High",
        "justification": "Explain the reason"
    }}

    Description:
    {description}

    Environment: {environment}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2
    )
    content = response.choices[0].message.content.strip()
    return safe_parse(content)

def generate_suggestions(description):
    """Suggest improvements for a CR description."""
    prompt = f"""
    You are a Change Management Reviewer.
    Suggest improvements for this CR. Return ONLY a JSON object:
    {{
        "suggestions": [
            "Suggestion 1",
            "Suggestion 2",
            "Suggestion 3"
        ]
    }}

    Description:
    {description}
    """
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.4
    )
    content = response.choices[0].message.content.strip()
    return safe_parse(content)
