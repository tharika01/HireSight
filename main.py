import json
from openai import AzureOpenAI
from structured_output.structured_output import ResumeChecklist
from config.config import OPENAI_API_KEY, azure_endpoint, azure_openai_api_version, azure_openai_model, setup_logger
from markitdown import MarkItDown

logger = setup_logger()

def main(file_path: str):
    md = MarkItDown()
    resume = md.convert(file_path)
    logger.info(f"Content extracted by mark it down from the resume \n {resume.text_content}")

    messages = [
        {
            "role": "system", 
            "content": '''You are a Senior Talent Acquisition Manager. 
                        Your job is to extract the candidates details exactly as it is provided in the resume without any mistakes. 
                        If you can find a particular piece of information simply return null.'''
        },
        {
            "role": "user", 
            "content": f"Candidates resume \n{resume}"},
    ]
    client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=OPENAI_API_KEY,
            api_version=azure_openai_api_version
        )
    response = client.beta.chat.completions.parse(
                model=azure_openai_model,
                messages=messages,
                temperature=0.2,
                response_format=ResumeChecklist
            )
    response = response.choices[0].message
    logger.info(f"candidate details extracted {response}")

    with open('results/generated_output', 'a') as output_file:
        json.dump(response.parsed.dict(), output_file, indent=4)
    return response.parsed.dict()

if __name__ == '__main__':
    main("sample_resumes/10030015.pdf")