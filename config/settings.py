# config/settings.py
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Slack Configuration
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_SIGNING_SECRET = os.getenv("SLACK_SIGNING_SECRET")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN") # Required for Socket Mode

# OpenAI Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_EMBEDDING_MODEL = "text-embedding-ada-002"
OPENAI_GPT_MODEL = "gpt-4" # Or your preferred model like "gpt-3.5-turbo"

# Pinecone Configuration
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME", "gutless-ai-assistant")
PINECONE_EMBEDDING_DIMENSION = 1536 # Dimension for text-embedding-ada-002

# Transcription Service (Example - if you use one)
# TRANSCRIPTION_API_KEY = os.getenv("TRANSCRIPTION_API_KEY")

# Application Settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO").upper()

# Validate essential configurations
def validate_config():
    required_vars = {
        "SLACK_BOT_TOKEN": SLACK_BOT_TOKEN,
        "SLACK_SIGNING_SECRET": SLACK_SIGNING_SECRET,
        "OPENAI_API_KEY": OPENAI_API_KEY,
        "PINECONE_API_KEY": PINECONE_API_KEY,
        "PINECONE_ENVIRONMENT": PINECONE_ENVIRONMENT,
    }
    # SLACK_APP_TOKEN is only required if using Socket Mode, which is the default in bot.py
    if not SLACK_APP_TOKEN:
        print("Warning: SLACK_APP_TOKEN is not set. Socket Mode will not work.")
        # You might choose to make this an error if Socket Mode is mandatory
        # raise ValueError("SLACK_APP_TOKEN is required for Socket Mode and is not set.")


    missing_vars = [key for key, value in required_vars.items() if not value]
    if missing_vars:
        raise ValueError(f"Missing essential configuration variables: {', '.join(missing_vars)}. Please set them in your .env file or environment.")

if __name__ == "__main__":
    try:
        validate_config()
        print("Configuration loaded and validated successfully.")
        print(f"OpenAI Model: {OPENAI_GPT_MODEL}")
        print(f"Pinecone Index: {PINECONE_INDEX_NAME}")
    except ValueError as e:
        print(f"Configuration Error: {e}")
