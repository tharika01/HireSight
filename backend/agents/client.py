from openai import AzureOpenAI
from backend.configurations.config import OPENAI_API_KEY, azure_endpoint, azure_openai_api_version, azure_openai_model, setup_logger

logger = setup_logger()

client = AzureOpenAI(
            azure_endpoint=azure_endpoint,
            api_key=OPENAI_API_KEY,
            api_version=azure_openai_api_version
        )