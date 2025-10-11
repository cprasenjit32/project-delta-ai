import streamlit as st
from llm_agent import validate_cr_description, assess_risk, generate_suggestions
from db_handler import save_to_db


st.set_page_config(page_title="Project Delta - CR Validator", layout="wide")
st.title("🚀 Project Delta - Change Request Validation Tool")

description = st.text_area("✏️ Enter CR Description")

if st.button("✅ Validate Description"):
    if description:
        result = validate_cr_description(description)
        st.success("Validation Result:")
        st.json(result)
    else:
        st.warning("Please enter a CR description.")

if st.button("🧠 Assess Risk"):
    if description:
        score, reason = assess_risk(description)
        st.info(f"**Risk Score:** {score}")
        st.write(reason)
    else:
        st.warning("Please enter a CR description.")

if st.button("💡 Show Suggestions to Fix Issues"):
    if description:
        suggestions = generate_suggestions(description)
        st.success("Suggestions:")
        for i, suggestion in enumerate(suggestions, 1):
            st.markdown(f"**{i}.** {suggestion}")
    else:
        st.warning("Please enter a CR description.")
