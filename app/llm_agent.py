import os
import openai

# Set API key
openai.api_key = os.getenv("OPENAI_API_KEY")

def validate_cr_description(description: str) -> str:
    prompt = f"""You are an IT Change Advisory Assistant.
Evaluate the following change request description and determine if it's clear, complete, and valid.

Description:
{description}

Respond with 'VALID' if it is complete and clearly describes the change. Otherwise, respond with 'INVALID' and mention why."""
    
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are an expert Change Management assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    
    return response['choices'][0]['message']['content'].strip()

def assess_risk(description: str) -> str:
    prompt = f"""Based on the change description below, assess the risk level as Low, Medium, or High, and justify your answer.

Description:
{description}

Respond in the format:
Risk Level: <Low/Medium/High>
Reason: <short reason>"""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Change Risk Analyst."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()

def generate_suggestions(description: str) -> str:
    prompt = f"""The following change request description was found invalid or incomplete:

{description}

Provide 3 helpful suggestions to improve it for validation."""

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant improving change request descriptions."},
            {"role": "user", "content": prompt}
        ]
    )

    return response['choices'][0]['message']['content'].strip()
