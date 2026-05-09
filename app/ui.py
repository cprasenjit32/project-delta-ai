import streamlit as st
import pandas as pd
from llm_agent import analyze_change_request
from db_handler import init_db, save_change_request, get_all_change_requests

st.set_page_config(
    page_title="Project Delta - AI Change Agent",
    page_icon="🚀",
    layout="wide"
)

init_db()

st.markdown("""
<style>
.main-title {
    font-size: 38px;
    font-weight: 800;
    color: #FF6B00;
}
.sub-title {
    font-size: 18px;
    color: #555;
}
.risk-low {
    background-color: #d4edda;
    color: #155724;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}
.risk-medium {
    background-color: #fff3cd;
    color: #856404;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}
.risk-high {
    background-color: #f8d7da;
    color: #721c24;
    padding: 10px;
    border-radius: 10px;
    font-weight: bold;
}
.card {
    background-color: #f8f9fa;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #ddd;
}
</style>
""", unsafe_allow_html=True)

st.sidebar.title("🚀 Project Delta")
page = st.sidebar.radio(
    "Navigation",
    ["AI Change Validator", "Saved Requests", "Architecture", "About"]
)

if page == "AI Change Validator":
    st.markdown('<div class="main-title">Project Delta</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="sub-title">AI Agent for Intelligent Change & Release Management</div>',
        unsafe_allow_html=True
    )

    st.divider()

    col1, col2 = st.columns([2, 1])

    with col1:
        change_text = st.text_area(
            "Change Request / Deployment Description",
            height=220,
            placeholder="Example: Deploy API changes to PROD for payment service..."
        )

    with col2:
        environment = st.selectbox(
            "Target Environment",
            ["DEV", "CIT", "UAT", "LLE", "PROD"]
        )

        rollback_plan = st.text_area(
            "Rollback Plan",
            height=160,
            placeholder="Example: Revert to previous build, restore DB backup..."
        )

    analyze_btn = st.button("🔍 Validate & Assess Risk", use_container_width=True)

    if analyze_btn:
        if not change_text.strip():
            st.error("Please enter a change request description.")
        else:
            with st.spinner("AI agents are analyzing the change request..."):
                result = analyze_change_request(change_text, environment, rollback_plan)

            risk = result["risk"]

            st.success("Analysis completed successfully.")

            c1, c2, c3 = st.columns(3)

            with c1:
                st.metric("Environment", environment)

            with c2:
                st.metric("Risk Level", risk)

            with c3:
                st.metric("CAB Decision", result["cab"])

            st.divider()

            if risk == "LOW":
                st.markdown('<div class="risk-low">LOW RISK - Standard approval recommended</div>', unsafe_allow_html=True)
            elif risk == "MEDIUM":
                st.markdown('<div class="risk-medium">MEDIUM RISK - Release Manager review required</div>', unsafe_allow_html=True)
            else:
                st.markdown('<div class="risk-high">HIGH RISK - CAB approval required</div>', unsafe_allow_html=True)

            st.subheader("🧠 AI Validation Output")
            st.markdown(result["validation"])

            st.subheader("✅ CAB Routing Recommendation")
            st.info(result["cab"])

            st.subheader("💡 AI Suggestions")
            st.markdown(result["suggestions"])

            save_change_request(
                change_text,
                environment,
                rollback_plan,
                risk,
                result["cab"]
            )

            st.success("Change request saved to local database.")

elif page == "Saved Requests":
    st.title("📁 Saved Change Requests")

    rows = get_all_change_requests()

    if rows:
        df = pd.DataFrame(
            rows,
            columns=["ID", "Environment", "Risk", "CAB Decision", "Created At"]
        )
        st.dataframe(df, use_container_width=True)
    else:
        st.info("No saved change requests yet.")

elif page == "Architecture":
    st.title("🏗️ Project Delta Architecture")

    st.markdown("""
```text
User
 ↓
Streamlit Dashboard
 ↓
AI Intake Agent
 ↓
Validation Agent
 ↓
Risk Assessment Agent
 ↓
CAB Decision Layer
 ↓
Suggestions Agent
 ↓
SQLite Database / Future ITSM Integration

```python
""")
