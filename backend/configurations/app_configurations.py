"""
This module contains the configuration settings for the application.
It includes the OpenAI API key, Azure OpenAI settings and logging configuration.
"""
import os
import logging
from dotenv import load_dotenv

load_dotenv()

MCP_SERVER_URL = os.getenv("MCP_SERVER_URL")

LOG_FILE="./logs/resume_parser.log"
os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)

def setup_logger(name: str = None):
    formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(name)s | %(message)s')

    handler = logging.FileHandler(LOG_FILE)
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setFormatter(formatter)

    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(handler)
        # logger.addHandler(console)

    return logger