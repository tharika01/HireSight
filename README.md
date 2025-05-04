# 🚀 HireSight

**AI-powered resume analysis and hiring assistant** using OpenAI Agents SDK + MCP (Model Context Protocol).

HireSight provides tools for both:

* 👩‍💼 **Recruiters**: Extract structured candidate data, simplify evaluation.
* 🙋‍♂️ **Candidates**: Get ATS scores, resume suggestions, and role recommendations.

---

## 🛠️ Getting Started

#### 1. Clone the repository

```bash
git https://github.com/tharika01/HireSight.git
cd HireSight
```

#### 2. Install [uv](https://github.com/astral-sh/uv) if not already installed

```bash
curl -Ls https://astral.sh/uv/install.sh | bash
```

#### 3. Create and activate a virtual environment

```bash
uv venv
source .venv/bin/activate  # Linux/macOS

# OR for Windows
.venv\Scripts\activate
```

#### 4. Install project dependencies

If you're using `requirements.txt`:

```bash
uv pip install -r requirements.txt
```

Or if using `pyproject.toml`:

```bash
uv pip install .
```

---
#### 5. Environment Configuration

Create a `.env` file in the project root with the following:

```dotenv
AZURE_OPENAI_KEY=your-key-here
AZURE_OPENAI_MODEL=gpt-4
OPENAI_API_BASE=https://your-endpoint.openai.azure.com
MCP_SERVER_URL="http://localhost:8000/mcp"
```
---

#### 6. ▶️ Running the MCP FastAPI Server

```bash
uvicorn backend.app:app --reload
```

Visit the interactive API docs at:
👉 `http://localhost:8000/docs`

---

## 📌 Roadmap

* [x] Resume parsing (single)
* [x] Recruiter tool integration
* [ ] Multi-resume batch processing
* [ ] Frontend dashboard (Streamlit)
* [ ] Candidate job-fit analyzer

---