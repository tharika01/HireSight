from fastapi import APIRouter
from backend.configurations.openai_client_config import get_client, azure_openai_model
from backend.schemas.openai_response_fromatter import ResumeChecklist
from backend.configurations.app_configurations import setup_logger

router = APIRouter()
logger = setup_logger()


@router.post("/parse", operation_id="parse_resume")
async def parse_resume(input):
    """
    Parse resume content to extract structured candidate information.

    This endpoint is a tool that accepts raw resume text (or Markdown-extracted content)
    and uses an LLM-based parser to extract structured candidate details such as:
    - Name
    - Email
    - Phone number
    - Education
    - Work experience
    - Skills
    - Any other relevant fields defined by the ResumeChecklist schema

    The parsing is performed using a language model (e.g., Azure OpenAI) with strict instructions
    to extract data exactly as it appears in the input. If any expected field is missing,
    the model will return `null` for that field.

    Args:
    -----
        input (str): The full resume content.

    Returns:
    --------
        dict: A dictionary of extracted resume fields conforming to the ResumeChecklist schema.

    Raises:
    -------
        Logs an error if any exception occurs during processing and returns None.
    """
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
        client = get_client()
        response = client.beta.chat.completions.parse(
                    model=azure_openai_model,
                    messages=messages,
                    temperature=0.2,
                    response_format=ResumeChecklist
                )
        response = response.choices[0].message
        logger.info(f"candidate details extracted {response}")

        return response.parsed.model_dump()
    except Exception as e:
        logger.error(f"Exception occurred while parsing resume : {e}")