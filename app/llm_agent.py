import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def validate_cr_description(description):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You're a Change Management expert."},
                  {"role": "user", "content": f"Validate this CR description: {description}"}]
    )
    return {"validation": response.choices[0].message.content.strip()}

def assess_risk(description):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You're a risk assessment engine."},
                  {"role": "user", "content": f"Rate the risk of this CR: {description}. Return only one word (Low, Medium, High) and explain."}]
    )
    content = response.choices[0].message.content.strip()
    if ":" in content:
        score, reason = content.split(":", 1)
        return score.strip(), reason.strip()
    return "Unknown", content

def generate_suggestions(description):
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You're a Change Review expert."},
                  {"role": "user", "content": f"Suggest improvements to this CR: {description}"}]
    )
    suggestions = response.choices[0].message.content.strip().split('\n')
    return [s.strip() for s in suggestions if s.strip()]
