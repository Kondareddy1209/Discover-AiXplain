import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch aiXplain API key
AIXPLAIN_API_KEY = os.getenv("AIXPLAIN_API_KEY")

if not AIXPLAIN_API_KEY:
    raise ValueError("AIXPLAIN_API_KEY is missing. Please set it in the .env file.")

def get_api_key():
    return AIXPLAIN_API_KEY
