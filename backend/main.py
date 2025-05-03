import io
from pypdf import PdfReader
from agents import Runner
from dotenv import load_dotenv
from agents.mcp import MCPServerSse
from fastapi_mcp import FastApiMCP
from fastapi.responses import JSONResponse
from fastapi import FastAPI,  UploadFile, File, Form
from backend.configurations.config import setup_logger
from backend.agents.agent_definitions import recruiter_agent
from backend.tools.resume_parser import router as parse_resume_router

load_dotenv()
logger = setup_logger()

app = FastAPI(title="AI Job Assistant")
app.include_router(parse_resume_router)
mcp = FastApiMCP(app, 
                 name="MCP server for AI Job Assistant",
                 include_operations=["parse_resume"])
mcp.mount()

@app.post("/recruiter/make_recruitment_decision")
async def match_profile(file: UploadFile = File(...), role: str = Form(...)):
    try:
        logger.info(f"file type uploaded {file.content_type}")
        if file.content_type != "application/pdf":
            return JSONResponse(content={"error": "Only PDF files are allowed"}, status_code=400)        

        # Read the uploaded PDF file
        file_content = await file.read()
        pdf_reader = PdfReader(io.BytesIO(file_content))

        # Extract text from each page
        extracted_text = ""
        for page in pdf_reader.pages:
            text = page.extract_text()
            if text:
                extracted_text += text + "\n"
                
        logger.info(f"file uploaded is {extracted_text}")
        async with MCPServerSse(params={"url": "http://localhost:8000/mcp"}) as mcp_server:
            tools = await mcp_server.list_tools()
            logger.info(tools)

            response = await Runner.run(recruiter_agent(mcp_server=[mcp_server]), f"Here is the resume:\n{extracted_text}\n\nThe candidate is applying for the role: {role} .\nShould we hire this person?")
            logger.info(response)

            return JSONResponse(content={"result": str(response.final_output), }, status_code=200)
    except Exception as e:
        return JSONResponse(content={"error" : str(e)}, status_code=400)
