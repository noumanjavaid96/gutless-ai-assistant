# Installation Guide

This guide will walk you through setting up the Renesis AI Assistant on your local machine or server.

## Prerequisites

- Python 3.8 or higher
- pip (Python package installer)
- Git
- Access to the following services:
  - OpenAI API (for GPT-4o and embeddings)
  - Pinecone (for vector database)
  - Slack workspace with bot creation permissions

## Step 1: Clone the Repository

```bash
git clone <repository-url>
cd gutless-ai-assistant
```

## Step 2: Create Virtual Environment

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

## Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

## Step 4: Environment Configuration

1. Copy the example environment file:
```bash
cp .env.example .env
```

2. Edit the `.env` file with your API keys and configuration:
```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o
OPENAI_EMBEDDING_MODEL=text-embedding-ada-002

# Pinecone Configuration
PINECONE_API_KEY=your_pinecone_api_key_here
PINECONE_ENVIRONMENT=your_pinecone_environment
PINECONE_INDEX_NAME=gutless-assistant

# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_SIGNING_SECRET=your_slack_signing_secret
SLACK_APP_TOKEN=xapp-your-slack-app-token

# Application Configuration
LOG_LEVEL=INFO
DEBUG=False
```

## Step 5: Set Up External Services

### OpenAI API
1. Visit [OpenAI Platform](https://platform.openai.com/)
2. Create an account or sign in
3. Generate an API key
4. Add the key to your `.env` file

### Pinecone
1. Visit [Pinecone](https://www.pinecone.io/)
2. Create an account
3. Create a new index with the following settings:
   - Dimensions: 1536 (for OpenAI embeddings)
   - Metric: cosine
   - Index name: `gutless-assistant`
4. Get your API key and environment
5. Add them to your `.env` file

### Slack App
1. Visit [Slack API](https://api.slack.com/apps)
2. Create a new app
3. Configure the following:
   - **OAuth & Permissions**: Add bot token scopes:
     - `app_mentions:read`
     - `chat:write`
     - `im:read`
     - `im:write`
   - **Event Subscriptions**: Enable and add:
     - `app_mention`
     - `message.im`
   - **Socket Mode**: Enable for development
4. Install the app to your workspace
5. Copy the tokens to your `.env` file

## Step 6: Initialize the Database

```bash
# Run the data ingestion script to set up initial content
python scripts/ingest_data.py
```

## Step 7: Run the Application

```bash
# Start the Slack bot
python src/bot.py
```

## Verification

1. Check that the bot appears online in your Slack workspace
2. Send a direct message to the bot or mention it in a channel
3. Verify that it responds appropriately

## Troubleshooting

If you encounter issues during installation:

1. **Python Version**: Ensure you're using Python 3.8+
2. **Dependencies**: Try upgrading pip: `pip install --upgrade pip`
3. **API Keys**: Verify all API keys are correct and have proper permissions
4. **Network**: Check firewall settings if running on a server

For more detailed troubleshooting, see our [Troubleshooting Guide](troubleshooting.md).

## Next Steps

- [Configuration Guide](configuration.md)
- [Usage Guide](usage.md)