import streamlit as st
from PIL import Image
import base64

# Load your image and convert to base64
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        encoded = base64.b64encode(img_file.read()).decode()
    return f"data:image/jpg;base64,{encoded}"

# Path to your local image
image_url = get_base64_image("frontend/assets/banner.jpg")


# --- Page Configuration ---
st.set_page_config(
    page_title="HireSight | AI for Recruitment & Resumes",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# --- Lilac Theme CSS ---
st.markdown(f"""
    <style>
    .title-container {{
        background-image: url('{image_url}');
        background-size: cover;
        background-position: center;
        padding: 2rem;
        border-radius: 1rem;
        text-align: center;
        margin-bottom: 2rem;
        color: white;
    }}
    .title-container h1, .title-container h2 {{
        color: white;
        text-shadow: 1px 1px 2px #000000;
    }}
    </style>

    <div class="title-container">
        <h3>Welcome to <strong>HireSight</strong></h3>
        <h4>AI-powered assistant for smarter hiring and job searching</h4>
    </div>
""", unsafe_allow_html=True)


# --- About Section ---
st.write("# 🔎 What is HireSight?")
st.markdown("""
## **HireSight** leverages AI to help both:

- ### 👩‍💼 **Recruiters**:    
    - Upload applicant resumes
    - Enter job requirements
    - Get a ranked list of candidates that best match the role — instantly!
            
- ### 🙋‍♂️ **Candidates** (Coming Soon ... ):    
    - Get an **ATS score** for your resume
    - Learn how to improve your fit for specific job roles
    - See which roles you're best suited for
    - Generate custom LinkedIn job search filters

> We simplify the recruitment journey using the power of AI !
""")

st.markdown("---")

# --- Navigation ---
st.header("🚀 Get Started")
st.page_link("pages/Recruiter.py", label="I'm a Recruiter", icon="🧑‍💼")
st.page_link("pages/Candidate.py", label="I'm a Candidate", icon="📄")

st.markdown("---")
st.caption("Built with Streamlit, FastAPI, and OpenAI Agents")
