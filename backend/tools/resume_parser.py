import json
from pydantic import BaseModel
from fastapi import APIRouter
from backend.configurations.openai_client_config import client
from backend.schemas.structured_output import ResumeChecklist
from backend.configurations.app_configurations import setup_logger, azure_openai_model

router = APIRouter()
logger = setup_logger()


@router.post("/parse", operation_id="parse_resume")
async def parse_resume(input):
    """Endpoint to parse resume"""
    logger.info(f"Content extracted by mark it down from the resume \n {input}")
    try:
        messages = [
            {
                "role": "system", 
                "content": '''You are a Senior Talent Acquisition Manager. 
                            Your job is to extract the candidates details exactly as it is provided in the resume without any mistakes. 
                            If you can find a particular piece of information simply return null.'''
            },
            {
                "role": "user", 
                "content": f"Candidates resume \n{input}"},
        ]
        
        response = client.beta.chat.completions.parse(
                    model=azure_openai_model,
                    messages=messages,
                    temperature=0.2,
                    response_format=ResumeChecklist
                )
        response = response.choices[0].message
        logger.info(f"candidate details extracted {response}")

        with open('results/generated_output.json', 'a') as output_file:
            json.dump(response.parsed.model_dump(), output_file, indent=4)
        return response.parsed.model_dump()
    except Exception as e:
        logger.error(f"Exception occurred while parsing resume : {e}")