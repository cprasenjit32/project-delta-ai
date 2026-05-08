# 🚀 Project Delta

## AI Agent for Intelligent Change & Release Management

Project Delta is an AI-powered Change & Release Management platform designed to automate deployment governance workflows using Large Language Models (LLMs) and intelligent agent-based validation.

Built for the AMD AI Hackathon.

---

# 📌 Problem Statement

Enterprise deployment and release management processes often involve:

- Poorly written change requests
- Missing rollback plans
- Manual CAB approvals
- High operational risk
- Failed deployments
- Delayed release cycles

Current governance processes are heavily manual and time-consuming.

Project Delta solves this problem using AI-assisted validation and intelligent risk assessment.

---

# 🧠 Features

## ✅ AI Change Validation
Analyzes deployment requests and identifies:
- Missing details
- Weak descriptions
- Incomplete rollback plans
- Governance gaps

---

## ⚠️ Risk Assessment Engine
Automatically classifies deployment risk:
- LOW
- MEDIUM
- HIGH

Based on:
- Environment
- Deployment complexity
- Risk keywords
- Rollback quality

---

## 🏛️ CAB Routing Recommendation
Provides governance recommendations:
- Standard approval
- Release Manager review
- CAB approval required

---

## 💡 Intelligent Suggestions
AI-generated recommendations for:
- Better deployment descriptions
- Rollback improvements
- Validation steps
- Governance readiness

---

# 🏗️ Architecture

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
```

---

# ⚙️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | Streamlit |
| Backend | Python |
| AI/LLM | OpenAI GPT |
| Database | SQLite |
| Version Control | GitHub |
| Future AI Scaling | AMD GPUs + vLLM |

---

# 🚀 Setup Instructions

## Clone Repository

```bash
git clone https://github.com/cprasenjit32/project-delta-ai.git
```

## Navigate to Project

```bash
cd project-delta-ai
```

## Create Virtual Environment

```bash
python -m venv venv
```

## Activate Virtual Environment

### macOS/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file or configure Streamlit secrets with:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app/ui.py
```

---

# 📷 Demo Workflow

1. Enter deployment/change request
2. Select target environment
3. Provide rollback plan
4. Click “Validate & Assess Risk”
5. Review:
   - Validation output
   - Risk level
   - CAB recommendation
   - AI suggestions

---

# 🧩 Example Use Case

### Input
Deploy payment API changes to PROD environment for authentication enhancement. Includes database schema updates and API gateway routing changes.

### Expected Output
- Risk Level: HIGH
- CAB Approval: Required
- Governance Suggestions: Generated
- Rollback Validation: Passed

---

# 🔮 Future Enhancements

- ServiceNow integration
- Freshdesk integration
- Jira integration
- Azure DevOps integration
- Predictive deployment failure detection
- RCA analysis agent
- MCP integrations
- Multi-agent orchestration
- AMD GPU-powered local inference
- vLLM model serving

---

# 🧠 AMD AI Alignment

Project Delta demonstrates how enterprise AI agents can automate governance workflows and deployment risk analysis.

Future scalability includes:
- Local LLM inference
- vLLM serving
- AMD Instinct GPU acceleration
- ROCm optimization
- Secure enterprise on-prem deployments

---

# 👨‍💻 Author

Built by Prasenjit Chow
