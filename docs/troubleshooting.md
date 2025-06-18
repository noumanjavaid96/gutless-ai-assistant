# Troubleshooting Guide

This guide helps you diagnose and resolve common issues with the Renesis AI Assistant.

## Quick Diagnostics

### Health Check Commands

Run these commands to quickly check system health:

```bash
# Test configuration loading
python -c "from config.settings import settings; print('✅ Configuration loaded')"

# Test API connections
python scripts/test_connections.py

# Check bot status
python -c "from src.bot import SlackBot; print('✅ Bot module imports successfully')"
```

### Common Status Indicators

| Status | Meaning | Action |
|--------|---------|--------|
| ✅ Bot online in Slack | Working correctly | None needed |
| ⚠️ Bot appears offline | Connection issue | Check tokens and network |
| ❌ Bot not responding | Critical error | Check logs and restart |
| 🔄 Slow responses | Performance issue | Check API rate limits |

## Installation Issues

### Python Version Problems

**Problem**: `SyntaxError` or compatibility issues

**Solution**:
```bash
# Check Python version
python --version
# Should be 3.8 or higher

# If using wrong version, create virtual environment with correct Python
python3.8 -m venv venv
# or
conda create -n gutless-assistant python=3.8
```

### Dependency Installation Failures

**Problem**: `pip install` fails with errors

**Solutions**:

1. **Upgrade pip**:
```bash
pip install --upgrade pip
```

2. **Clear pip cache**:
```bash
pip cache purge
```

3. **Install with verbose output**:
```bash
pip install -r requirements.txt -v
```

4. **Platform-specific issues**:
```bash
# Windows: Install Visual C++ Build Tools
# macOS: Install Xcode command line tools
xcode-select --install
# Linux: Install build essentials
sudo apt-get install build-essential
```

### Virtual Environment Issues

**Problem**: Packages not found or wrong versions

**Solution**:
```bash
# Deactivate and recreate virtual environment
deactivate
rm -rf venv  # or rmdir /s venv on Windows
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

## Configuration Issues

### Environment Variables Not Loading

**Problem**: `KeyError` or `None` values for environment variables

**Diagnosis**:
```bash
# Check if .env file exists
ls -la .env

# Check environment variable loading
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print(os.getenv('OPENAI_API_KEY')[:10] if os.getenv('OPENAI_API_KEY') else 'Not found')"
```

**Solutions**:

1. **Create .env file**:
```bash
cp .env.example .env
# Edit .env with your actual values
```

2. **Check file format**:
```env
# Correct format (no spaces around =)
OPENAI_API_KEY=sk-your-key-here

# Incorrect format
OPENAI_API_KEY = sk-your-key-here
```

3. **Verify file location**:
```bash
# .env should be in project root
gutless-ai-assistant/
├── .env  ← Here
├── src/
└── docs/
```

### Invalid API Keys

**Problem**: Authentication errors from external APIs

**Diagnosis**:
```bash
# Test OpenAI key
curl -H "Authorization: Bearer $OPENAI_API_KEY" https://api.openai.com/v1/models

# Test Pinecone key
python -c "import pinecone; pinecone.init(api_key='your-key', environment='your-env'); print('✅ Pinecone connected')"
```

**Solutions**:

1. **Regenerate API keys** from respective platforms
2. **Check key format**:
   - OpenAI: `sk-...` (starts with sk-)
   - Pinecone: UUID format
   - Slack Bot: `xoxb-...`
   - Slack App: `xapp-...`

3. **Verify permissions** on API keys

## Slack Integration Issues

### Bot Not Responding

**Problem**: Bot appears online but doesn't respond to messages

**Diagnosis**:
```bash
# Check bot logs
tail -f logs/app.log

# Test bot locally
python src/bot.py
```

**Solutions**:

1. **Check Event Subscriptions**:
   - Go to Slack App settings
   - Verify `app_mention` and `message.im` events are enabled
   - Check Request URL is correct

2. **Verify Bot Permissions**:
   - `app_mentions:read`
   - `chat:write`
   - `im:read`
   - `im:write`

3. **Socket Mode Issues**:
```python
# Enable Socket Mode in Slack app settings
# Ensure SLACK_APP_TOKEN is set
# Check if port 3000 is available
```

### Bot Responds with Errors

**Problem**: Bot sends error messages instead of answers

**Common Error Messages**:

| Error Message | Cause | Solution |
|---------------|-------|----------|
| "I'm having trouble processing your request" | General error | Check logs for specific error |
| "No relevant content found" | Empty search results | Check content ingestion |
| "Service temporarily unavailable" | API rate limit or outage | Wait and retry |
| "Invalid query format" | Query preprocessing error | Rephrase question |

### Permission Denied Errors

**Problem**: Bot can't send messages or access channels

**Solution**:
1. **Reinstall bot** to workspace
2. **Check channel permissions**:
   - Invite bot to private channels
   - Verify bot has write permissions
3. **Update OAuth scopes** if needed

## API Integration Issues

### OpenAI API Problems

**Rate Limit Exceeded**:
```
Error: Rate limit exceeded
```

**Solutions**:
- Implement exponential backoff (already included)
- Reduce request frequency
- Upgrade OpenAI plan
- Check for infinite loops in code

**Invalid Model Access**:
```
Error: The model 'gpt-4o' does not exist
```

**Solutions**:
- Verify model name in configuration
- Check OpenAI account has access to GPT-4
- Use alternative model (gpt-3.5-turbo)

**Token Limit Exceeded**:
```
Error: This model's maximum context length is X tokens
```

**Solutions**:
- Reduce context size in queries
- Implement context truncation
- Split large queries

### Pinecone Issues

**Index Not Found**:
```
Error: Index 'gutless-assistant' not found
```

**Solutions**:
1. **Create index**:
```python
import pinecone
pinecone.init(api_key="your-key", environment="your-env")
pinecone.create_index(
    name="gutless-assistant",
    dimension=1536,
    metric="cosine"
)
```

2. **Check index name** in configuration

**Connection Timeout**:
```
Error: Connection timeout
```

**Solutions**:
- Check network connectivity
- Verify Pinecone environment setting
- Implement retry logic

**Quota Exceeded**:
```
Error: Quota exceeded
```

**Solutions**:
- Upgrade Pinecone plan
- Optimize vector storage
- Implement batch operations

## Content Ingestion Issues

### Transcription Failures

**Problem**: Audio/video files not transcribing

**Diagnosis**:
```bash
# Check file format
file audio_file.mp3

# Check file size
ls -lh audio_file.mp3

# Test transcription manually
python -c "from src.content_ingestion.transcribe import TranscriptionService; ts = TranscriptionService(); result = ts.transcribe_file('path/to/file')"
```

**Solutions**:

1. **Supported formats**: mp3, wav, m4a, mp4
2. **File size limit**: 25MB for Whisper
3. **Audio quality**: Ensure clear audio
4. **File path**: Use absolute paths

### PDF Processing Issues

**Problem**: PDF content not extracting properly

**Common Issues**:
- Scanned PDFs (image-based)
- Password-protected PDFs
- Corrupted files
- Complex layouts

**Solutions**:
```python
# Test PDF extraction
from src.content_ingestion.pdf_parser import PDFParser
parser = PDFParser()
content = parser.extract_text("path/to/file.pdf")
print(content.text[:500])  # First 500 characters
```

### Embedding Generation Failures

**Problem**: Embeddings not generating for content

**Diagnosis**:
```python
# Test embedding service
from src.embedding_service import EmbeddingService
service = EmbeddingService(api_key="your-key")
vector = service.generate_embedding("test text")
print(f"Embedding dimension: {len(vector)}")
```

**Solutions**:
- Check OpenAI API key
- Verify text is not empty
- Handle special characters
- Check text length limits

## Performance Issues

### Slow Response Times

**Problem**: Bot takes too long to respond

**Diagnosis**:
```bash
# Check response times in logs
grep "processing_time" logs/app.log

# Monitor API response times
grep "openai_response_time" logs/app.log
grep "pinecone_response_time" logs/app.log
```

**Solutions**:

1. **Optimize vector search**:
   - Reduce `top_k` value
   - Add metadata filters
   - Use smaller embedding dimensions

2. **Implement caching**:
   - Cache frequent queries
   - Cache embeddings
   - Use Redis for session storage

3. **Optimize content chunks**:
   - Reduce chunk size
   - Improve chunk quality
   - Remove irrelevant content

### Memory Issues

**Problem**: High memory usage or out-of-memory errors

**Solutions**:

1. **Batch processing**:
```python
# Process in smaller batches
for batch in chunks(large_list, batch_size=100):
    process_batch(batch)
```

2. **Memory monitoring**:
```python
import psutil
print(f"Memory usage: {psutil.virtual_memory().percent}%")
```

3. **Garbage collection**:
```python
import gc
gc.collect()
```

## Logging and Debugging

### Enable Debug Logging

```python
# In .env file
LOG_LEVEL=DEBUG
DEBUG=True

# Or programmatically
import logging
logging.getLogger().setLevel(logging.DEBUG)
```

### Log File Locations

```bash
# Application logs
tail -f logs/app.log

# Error logs
tail -f logs/error.log

# Slack events
tail -f logs/slack.log
```

### Debug Commands

```bash
# Test individual components
python -m src.embedding_service
python -m src.pinecone_service
python -m src.core_logic

# Run with debug output
python -u src/bot.py 2>&1 | tee debug.log
```

## Getting Help

### Before Asking for Help

1. **Check logs** for specific error messages
2. **Search this guide** for similar issues
3. **Test individual components** to isolate the problem
4. **Gather system information**:
   - Python version
   - Operating system
   - Package versions
   - Error messages

### Information to Include

When reporting issues, include:

```bash
# System information
python --version
pip list | grep -E "(openai|pinecone|slack)"

# Error logs (last 50 lines)
tail -50 logs/app.log

# Configuration (without sensitive data)
env | grep -E "(OPENAI|PINECONE|SLACK)" | sed 's/=.*/=****/'
```

### Emergency Procedures

**If bot is completely unresponsive**:

1. **Restart the application**:
```bash
# Stop current process
Ctrl+C

# Restart
python src/bot.py
```

2. **Reset to known good state**:
```bash
# Pull latest code
git pull origin main

# Reinstall dependencies
pip install -r requirements.txt --force-reinstall

# Clear cache
rm -rf __pycache__ src/__pycache__
```

3. **Fallback configuration**:
```env
# Use basic settings
OPENAI_MODEL=gpt-3.5-turbo
PINECONE_TOP_K=3
LOG_LEVEL=INFO
```

## Next Steps

- [FAQ](faq.md)

- [API Reference](api-reference.md)
- [Configuration Guide](configuration.md)