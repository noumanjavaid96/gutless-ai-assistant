# 🚀 Deployment Quick Start

This document provides a quick overview of deployment options for the Renesis AI Assistant. For detailed instructions, see the [complete deployment guide](docs/deployment.md).

## Prerequisites

- Docker and Docker Compose
- Slack workspace with bot permissions
- API keys: Slack, OpenAI, Pinecone

## Quick Deploy (Recommended)

### 1. Setup Environment

```bash
# Clone repository
git clone <repository-url>
cd gutless-ai-assistant

# Copy and edit environment file
cp .env.example .env
# Edit .env with your API keys
```

### 2. Deploy with Scripts

**Linux/macOS:**
```bash
chmod +x deploy.sh
./deploy.sh setup
./deploy.sh start
```

**Windows (PowerShell):**
```powershell
.\deploy.ps1 setup
.\deploy.ps1 start
```

### 3. Verify Deployment

```bash
# Check status
./deploy.sh status  # Linux/macOS
.\deploy.ps1 status  # Windows

# View logs
./deploy.sh logs    # Linux/macOS
.\deploy.ps1 logs    # Windows
```

## Alternative Deployment Methods

### Docker Compose (Manual)

```bash
docker-compose up -d
docker-compose logs -f gutless-ai-assistant
```

### Cloud Platforms

- **AWS ECS/Fargate**: Container orchestration
- **Google Cloud Run**: Serverless containers
- **Azure Container Instances**: Simple container hosting
- **Heroku**: Platform-as-a-Service

### Kubernetes

```bash
kubectl apply -f k8s/
```

## Environment Variables

Required environment variables:

```bash
# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
SLACK_APP_TOKEN=xapp-your-app-token

# AI Services
OPENAI_API_KEY=sk-your-openai-key
PINECONE_API_KEY=your-pinecone-key
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=gutless-ai-assistant
```

## CI/CD

GitHub Actions workflow automatically:
- Tests code changes
- Builds Docker images
- Deploys to staging/production
- Scans for security vulnerabilities

## Monitoring

```bash
# View application logs
docker-compose logs -f gutless-ai-assistant

# Check container health
docker-compose ps

# Monitor resource usage
docker stats
```

## Troubleshooting

### Common Issues

1. **Missing environment variables**: Check `.env` file
2. **API key errors**: Verify keys are valid
3. **Container won't start**: Check Docker logs
4. **Slack connection issues**: Verify bot permissions

### Debug Mode

```bash
# Enable debug logging
echo "LOG_LEVEL=DEBUG" >> .env
echo "DEVELOPMENT_MODE=true" >> .env

# Restart application
./deploy.sh restart
```

## Support

- 📖 [Complete Deployment Guide](docs/deployment.md)
- 🔧 [Troubleshooting Guide](docs/troubleshooting.md)
- 🏗️ [Architecture Overview](docs/architecture.md)
- 💬 [Contributing Guide](docs/contributing.md)

## Security Notes

- Never commit API keys to version control
- Use environment variables for secrets
- Regularly rotate API keys
- Monitor for security vulnerabilities
- Use HTTPS for all external communications

---

**Need help?** Check the [troubleshooting guide](docs/troubleshooting.md) or review the application logs for error details.