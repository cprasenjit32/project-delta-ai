import os
from openai import OpenAI

def get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")

    try:
        import streamlit as st
        api_key = st.secrets.get("OPENAI_API_KEY", api_key)
    except Exception:
        pass

    if not api_key:
        return None

    return OpenAI(api_key=api_key)


def fallback_analysis(change_text, environment, rollback_plan):
    text = f"{change_text} {environment} {rollback_plan}".lower()

    issues = []
    risk_score = 0

    if not change_text or len(change_text.strip()) < 30:
        issues.append("Change description is too short or unclear.")
        risk_score += 2

    if environment.upper() == "PROD":
        risk_score += 3

    if not rollback_plan or len(rollback_plan.strip()) < 20:
        issues.append("Rollback plan is missing or weak.")
        risk_score += 3

    risky_words = ["database", "schema", "payment", "auth", "login", "prod", "migration", "firewall"]
    for word in risky_words:
        if word in text:
            risk_score += 1

    if risk_score >= 6:
        risk = "HIGH"
        cab = "CAB approval required"
    elif risk_score >= 3:
        risk = "MEDIUM"
        cab = "Team lead / release manager review required"
    else:
        risk = "LOW"
        cab = "Eligible for standard approval"

    if not issues:
        issues.append("No major validation issues found.")

    suggestions = [
        "Add clear deployment steps.",
        "Mention impacted application/components.",
        "Include pre-validation and post-validation checks.",
        "Provide a tested rollback plan.",
        "Confirm business approval and release window."
    ]

    return {
        "validation": "\n".join(f"- {i}" for i in issues),
        "risk": risk,
        "cab": cab,
        "suggestions": "\n".join(f"- {s}" for s in suggestions)
    }


def analyze_change_request(change_text, environment, rollback_plan):
    client = get_openai_client()

    if client is None:
        return fallback_analysis(change_text, environment, rollback_plan)

    prompt = f"""
You are an expert IT Change and Release Management AI Agent.

Analyze this deployment change request.

Environment: {environment}

Change Request:
{change_text}

Rollback Plan:
{rollback_plan}

Return response in this exact format:

VALIDATION:
- Point 1
- Point 2

RISK:
LOW / MEDIUM / HIGH

CAB_DECISION:
Decision here

SUGGESTIONS:
- Suggestion 1
- Suggestion 2
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a Change and Release Management AI Agent."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )

        output = response.choices[0].message.content

        risk = "MEDIUM"
        if "RISK:" in output:
            if "HIGH" in output.upper():
                risk = "HIGH"
            elif "LOW" in output.upper():
                risk = "LOW"

        if risk == "HIGH":
            cab = "CAB approval required"
        elif risk == "MEDIUM":
            cab = "Release Manager / Team review required"
        else:
            cab = "Eligible for standard approval"

        return {
            "validation": output,
            "risk": risk,
            "cab": cab,
            "suggestions": output
        }

    except Exception as e:
        result = fallback_analysis(change_text, environment, rollback_plan)
        result["validation"] += f"\n\nLLM fallback used due to error: {str(e)}"
        return result
