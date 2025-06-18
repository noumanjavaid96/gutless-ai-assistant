# Configuration Guide

This guide covers all configuration options for the Renesis AI Assistant.

## Environment Variables

The application uses environment variables for configuration. These should be set in a `.env` file in the project root.

### Required Configuration

#### OpenAI Settings
```env
# OpenAI API key (required)
OPENAI_API_KEY=sk-...

# Model for answer generation (default: gpt-4o)
OPENAI_MODEL=gpt-4o

# Model for generating embeddings (default: text-embedding-ada-002)
OPENAI_EMBEDDING_MODEL=text-embedding-ada-002

# Maximum tokens for responses (default: 1000)
OPENAI_MAX_TOKENS=1000

# Temperature for response generation (default: 0.7)
OPENAI_TEMPERATURE=0.7
```

#### Pinecone Settings
```env
# Pinecone API key (required)
PINECONE_API_KEY=...

# Pinecone environment (required)
PINECONE_ENVIRONMENT=us-west1-gcp

# Index name for storing embeddings (default: gutless-assistant)
PINECONE_INDEX_NAME=gutless-assistant

# Number of similar chunks to retrieve (default: 5)
PINECONE_TOP_K=5

# Similarity threshold for results (default: 0.7)
PINECONE_SCORE_THRESHOLD=0.7
```

#### Slack Settings
```env
# Slack bot token (required)
SLACK_BOT_TOKEN=xoxb-...

# Slack signing secret (required)
SLACK_SIGNING_SECRET=...

# Slack app token for Socket Mode (required for development)
SLACK_APP_TOKEN=xapp-...

# Port for Slack events (default: 3000)
SLACK_PORT=3000
```

### Optional Configuration

#### Application Settings
```env
# Log level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
LOG_LEVEL=INFO

# Enable debug mode (True/False)
DEBUG=False

# Maximum content chunk size in characters (default: 1000)
MAX_CHUNK_SIZE=1000

# Chunk overlap size in characters (default: 200)
CHUNK_OVERLAP=200
```

#### Content Processing
```env
# Transcription service (whisper, assemblyai)
TRANSCRIPTION_SERVICE=whisper

# AssemblyAI API key (if using AssemblyAI)
ASSEMBLYAI_API_KEY=...

# Audio file formats to process
SUPPORTED_AUDIO_FORMATS=mp3,wav,m4a,mp4

# PDF processing options
PDF_EXTRACT_IMAGES=False
PDF_EXTRACT_TABLES=True
```

## Configuration File

Advanced configuration can be managed through `config/settings.py`:

```python
# config/settings.py
import os
from typing import List, Optional

class Settings:
    # OpenAI Configuration
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    OPENAI_MODEL: str = os.getenv("OPENAI_MODEL", "gpt-4o")
    OPENAI_EMBEDDING_MODEL: str = os.getenv("OPENAI_EMBEDDING_MODEL", "text-embedding-ada-002")
    OPENAI_MAX_TOKENS: int = int(os.getenv("OPENAI_MAX_TOKENS", "1000"))
    OPENAI_TEMPERATURE: float = float(os.getenv("OPENAI_TEMPERATURE", "0.7"))
    
    # Pinecone Configuration
    PINECONE_API_KEY: str = os.getenv("PINECONE_API_KEY")
    PINECONE_ENVIRONMENT: str = os.getenv("PINECONE_ENVIRONMENT")
    PINECONE_INDEX_NAME: str = os.getenv("PINECONE_INDEX_NAME", "gutless-assistant")
    PINECONE_TOP_K: int = int(os.getenv("PINECONE_TOP_K", "5"))
    PINECONE_SCORE_THRESHOLD: float = float(os.getenv("PINECONE_SCORE_THRESHOLD", "0.7"))
    
    # Slack Configuration
    SLACK_BOT_TOKEN: str = os.getenv("SLACK_BOT_TOKEN")
    SLACK_SIGNING_SECRET: str = os.getenv("SLACK_SIGNING_SECRET")
    SLACK_APP_TOKEN: str = os.getenv("SLACK_APP_TOKEN")
    SLACK_PORT: int = int(os.getenv("SLACK_PORT", "3000"))
    
    # Application Configuration
    LOG_LEVEL: str = os.getenv("LOG_LEVEL", "INFO")
    DEBUG: bool = os.getenv("DEBUG", "False").lower() == "true"
    MAX_CHUNK_SIZE: int = int(os.getenv("MAX_CHUNK_SIZE", "1000"))
    CHUNK_OVERLAP: int = int(os.getenv("CHUNK_OVERLAP", "200"))
    
    # Content Processing
    TRANSCRIPTION_SERVICE: str = os.getenv("TRANSCRIPTION_SERVICE", "whisper")
    ASSEMBLYAI_API_KEY: Optional[str] = os.getenv("ASSEMBLYAI_API_KEY")
    SUPPORTED_AUDIO_FORMATS: List[str] = os.getenv("SUPPORTED_AUDIO_FORMATS", "mp3,wav,m4a,mp4").split(",")
    PDF_EXTRACT_IMAGES: bool = os.getenv("PDF_EXTRACT_IMAGES", "False").lower() == "true"
    PDF_EXTRACT_TABLES: bool = os.getenv("PDF_EXTRACT_TABLES", "True").lower() == "true"

settings = Settings()
```

## Slack Bot Configuration

### Bot Permissions
Ensure your Slack bot has the following OAuth scopes:

- `app_mentions:read` - Read messages that mention the bot
- `chat:write` - Send messages
- `im:read` - Read direct messages
- `im:write` - Send direct messages
- `files:read` - Read file information (if file upload support is needed)

### Event Subscriptions
Configure the following events in your Slack app:

- `app_mention` - When the bot is mentioned
- `message.im` - Direct messages to the bot

### Socket Mode (Development)
For development, enable Socket Mode in your Slack app settings. This allows the bot to receive events without exposing a public endpoint.

## Pinecone Index Configuration

### Index Settings
When creating your Pinecone index, use these settings:

```json
{
  "name": "gutless-assistant",
  "dimension": 1536,
  "metric": "cosine",
  "pods": 1,
  "replicas": 1,
  "pod_type": "p1.x1"
}
```

### Metadata Schema
The following metadata fields are stored with each vector:

```json
{
  "source": "video_name_or_pdf_name",
  "content_type": "transcript|pdf",
  "timestamp_start": "00:05:30",
  "timestamp_end": "00:07:45",
  "chunk_index": 0,
  "text": "original_text_content"
}
```

## Logging Configuration

Logging is configured in `src/utils/logging_config.py`. You can customize:

- Log levels (DEBUG, INFO, WARNING, ERROR, CRITICAL)
- Log format
- Output destinations (console, file, external services)

```python
# Example logging configuration
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(),
        logging.FileHandler('logs/app.log')
    ]
)
```

## Security Considerations

1. **API Keys**: Never commit API keys to version control
2. **Environment Files**: Add `.env` to `.gitignore`
3. **Production**: Use secure secret management in production
4. **Slack Tokens**: Rotate tokens regularly
5. **Network**: Use HTTPS for all external communications

## Validation

To validate your configuration:

```bash
# Test configuration
python -c "from config.settings import settings; print('Configuration loaded successfully')"

# Test API connections
python scripts/test_connections.py
```

## Environment-Specific Configuration

### Development
```env
DEBUG=True
LOG_LEVEL=DEBUG
SLACK_PORT=3000
```

### Production
```env
DEBUG=False
LOG_LEVEL=INFO
SLACK_PORT=80
```

### Testing
```env
DEBUG=True
LOG_LEVEL=DEBUG
PINECONE_INDEX_NAME=gutless-assistant-test
```

## Next Steps

- [Usage Guide](usage.md)

- [Troubleshooting](troubleshooting.md)