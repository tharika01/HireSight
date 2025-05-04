import os
import streamlit as st
import requests

BASE_URL = os.getenv("API_BASE_URL", "http://127.0.0.1:8000")

# --- Page Config ---
st.set_page_config(page_title="HireSight | Recruiter", layout="wide")

st.title("🧑‍💼 Recruiter Dashboard")
st.markdown("Upload a candidate's resume and enter the role you're hiring for to get an AI-powered hiring recommendation.")
st.markdown("---")

# --- Click State ---
if 'clicked' not in st.session_state:
    st.session_state.clicked = False

def click_button():
    st.session_state.clicked = True

# --- Layout Columns ---
col1, col2 = st.columns([5, 5])

# --- Input Form ---
with col1:
    with st.form('job_description'):
        st.subheader("Job Details")
        role = st.text_input(
            label="Role Title",
            placeholder="e.g. Software Engineer, Marketing Manager"
        )

        uploaded_file = st.file_uploader(
            label="📎 Upload Candidate Resume (PDF only)",
            type="pdf"
        )

        submit = st.form_submit_button("🚀 Submit for Review", on_click=click_button)
        st.markdown("""
            <style>
                div.stButton > button {
                    display: block;
                    margin: 0 auto;
                }
            </style>
        """, unsafe_allow_html=True)

# --- Decision Output ---
col2.subheader("AI Hiring Recommendation")

if st.session_state.clicked:
    if uploaded_file is not None and role.strip():
        with st.spinner("Analyzing resume and generating decision..."):
            url = f"{BASE_URL}/recruiter/make_recruitment_decision"

            files = {
                "file": (uploaded_file.name, uploaded_file.getvalue(), "application/pdf")
            }
            payload = {
                "role": role
            }

            response = requests.post(url=url, data=payload, files=files)

        if response.status_code == 200:
            result = response.json()
            decision = result.get("decision", "Undecided")
            reason = result.get("reason", "No reason provided.")
            if decision.lower() == "hire":
                col2.success(f"**Decision**: {decision} ✅")
                col2.markdown(f"**Reason:**\n\n{reason}")
            else:
                col2.error(f"**Decision**: {decision} ❌ ")
                col2.markdown(f"**📝 Reason:**\n\n{reason}")
        else:
            col2.error("Error from server")
            col2.write(response.text)
    else:
        col2.warning("Please enter a role and upload a valid resume.")
