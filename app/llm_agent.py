import os
import openai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Validate the CR description using GPT-4
def validate_cr_description(description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a Change Management expert."},
            {"role": "user", "content": f"Validate this CR description: {description}"}
        ]
    )
    return {"validation": response.choices[0].message.content.strip()}

# Assess risk of a CR using GPT-4
def assess_risk(description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a risk assessment engine."},
            {"role": "user", "content": f"Rate the risk of this CR: {description}. Return only one word (Low, Medium, High) and explain."}
        ]
    )
    content = response.choices[0].message.content.strip()
    if ":" in content:
        score, reason = content.split(":", 1)
        return score.strip(), reason.strip()
    return "Unknown", content

# Generate suggestions for CR improvements using GPT-4
def generate_suggestions(description):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You're a Change Review expert."},
            {"role": "user", "content": f"Suggest improvements to this CR: {description}"}
        ]
    )
    suggestions = response.choices[0].message.content.strip().split('\n')
    return [s.strip() for s in suggestions if s.strip()]
