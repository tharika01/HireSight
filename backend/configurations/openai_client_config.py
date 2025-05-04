import os
from openai import AzureOpenAI, OpenAI
from dotenv import load_dotenv
from backend.configurations.app_configurations import setup_logger

load_dotenv()

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
azure_openai_api_version = os.getenv("AZURE_OPENAI_API_VERSION")
azure_openai_model = os.getenv("AZURE_OPENAI_DEPLOYMENT")

logger = setup_logger()

def get_client():
    if azure_endpoint and azure_openai_api_version:
        try:
            # Try Azure client
            client = AzureOpenAI(
                azure_endpoint=azure_endpoint,
                api_key=OPENAI_API_KEY,
                api_version=azure_openai_api_version
            )
            # Make a small test call to ensure the key works
            client.models.list()  # or another cheap request
            logger.info("Using AzureOpenAI")
            return client
        except Exception as e:
            logger.warning(f"AzureOpenAI failed: {e}")
            logger.warning("Falling back to OpenAI")

    # Fallback to OpenAI
    client = OpenAI(api_key=OPENAI_API_KEY)
    logger.info("Using OpenAI")
    return client
