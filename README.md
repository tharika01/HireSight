# 🚀 HireSight

**AI-powered resume analysis and hiring assistant** using OpenAI Agents SDK + MCP (Model Context Protocol).

HireSight provides tools for both:

* 👩‍💼 **Recruiters**: Extract structured candidate data, simplify evaluation.
* 🙋‍♂️ **Candidates**: Get ATS scores, resume suggestions, and role recommendations.

---

## 📦 Features

* ✅ Resume parsing via LLM
* ✅ Recruiter-facing structured data extraction
* ✅ Candidate-facing ATS feedback and role-fit analysis
* 🔜 Multi-resume upload support
* 🔌 Built with FastAPI + MCP + OpenAI Agents SDK
* ⚡ Powered by `uv` for fast dependency management and virtual environments

---

## 🛠️ Getting Started

### 1. Clone the repository

```bash
git https://github.com/tharika01/ApplySmart.git
cd ApplySmart
```

### 2. Install [uv](https://github.com/astral-sh/uv) if not already installed

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

### 3. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate  # Linux/macOS

# OR for Windows
.venv\Scripts\activate
```

### 4. Install project dependencies

If you're using `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

Or if using `pyproject.toml`:

```bash
uv pip install .
```

---

## ▶️ Running the MCP FastAPI Server

```bash
uvicorn app.main:app --reload
```

Visit the interactive API docs at:
👉 `http://localhost:8000/docs`

---

## ⚙️ Environment Configuration

Create a `.env` file in the project root with the following:

```dotenv
AZURE_OPENAI_KEY=your-key-here
AZURE_OPENAI_MODEL=gpt-4
OPENAI_API_BASE=https://your-endpoint.openai.azure.com
MCP_SERVER_URL="http://localhost:8000/mcp"
```

---

## 📌 Roadmap

* [x] Resume parsing (single)
* [x] Recruiter tool integration
* [ ] Multi-resume batch processing
* [ ] Frontend dashboard (Streamlit)
* [ ] Candidate job-fit analyzer

---