# Deployment Guide

This guide covers various deployment options for the Renesis AI Assistant Slack bot.

## Overview

The Renesis AI Assistant can be deployed in several ways:

- **Local Development**: Using Docker Compose for local testing
- **Cloud Platforms**: Deploy to AWS, Google Cloud, Azure, or Heroku
- **Container Orchestration**: Using Kubernetes or Docker Swarm
- **Serverless**: Using AWS Lambda, Google Cloud Functions, or Azure Functions

## Prerequisites

### Required Software

- [Docker](https://docs.docker.com/get-docker/) and [Docker Compose](https://docs.docker.com/compose/install/)
- [Git](https://git-scm.com/downloads)
- A Slack workspace with bot creation permissions

### Required API Keys

- **Slack Bot Token** (`SLACK_BOT_TOKEN`)
- **Slack Signing Secret** (`SLACK_SIGNING_SECRET`)
- **Slack App Token** (`SLACK_APP_TOKEN`) for Socket Mode
- **OpenAI API Key** (`OPENAI_API_KEY`)
- **Pinecone API Key** (`PINECONE_API_KEY`)

## Quick Start (Docker Compose)

### 1. Clone and Setup

```bash
# Clone the repository
git clone <repository-url>
cd gutless-ai-assistant

# Copy environment template
cp .env.example .env
```

### 2. Configure Environment

Edit the `.env` file with your actual API keys:

```bash
# Slack Configuration
SLACK_BOT_TOKEN=xoxb-your-bot-token-here
SLACK_SIGNING_SECRET=your-signing-secret-here
SLACK_APP_TOKEN=xapp-your-app-token-here

# OpenAI Configuration
OPENAI_API_KEY=sk-your-openai-api-key-here

# Pinecone Configuration
PINECONE_API_KEY=your-pinecone-api-key-here
PINECONE_ENVIRONMENT=us-west1-gcp
PINECONE_INDEX_NAME=gutless-ai-assistant
```

### 3. Deploy Using Scripts

#### Linux/macOS

```bash
# Make script executable
chmod +x deploy.sh

# Setup and start
./deploy.sh setup
./deploy.sh start

# View logs
./deploy.sh logs
```

#### Windows (PowerShell)

```powershell
# Setup and start
.\deploy.ps1 setup
.\deploy.ps1 start

# View logs
.\deploy.ps1 logs
```

### 4. Manual Docker Compose

```bash
# Build and start
docker-compose up -d

# View logs
docker-compose logs -f gutless-ai-assistant

# Stop
docker-compose down
```

## Cloud Platform Deployment

### AWS Deployment

#### Option 1: AWS ECS (Recommended)

1. **Create ECS Cluster**:
   ```bash
   aws ecs create-cluster --cluster-name gutless-ai-assistant
   ```

2. **Create Task Definition**:
   ```json
   {
     "family": "gutless-ai-assistant",
     "networkMode": "awsvpc",
     "requiresCompatibilities": ["FARGATE"],
     "cpu": "256",
     "memory": "512",
     "executionRoleArn": "arn:aws:iam::ACCOUNT:role/ecsTaskExecutionRole",
     "containerDefinitions": [
       {
         "name": "gutless-ai-assistant",
         "image": "ghcr.io/your-username/gutless-ai-assistant:latest",
         "essential": true,
         "environment": [
           {"name": "SLACK_BOT_TOKEN", "value": "${SLACK_BOT_TOKEN}"},
           {"name": "SLACK_SIGNING_SECRET", "value": "${SLACK_SIGNING_SECRET}"},
           {"name": "SLACK_APP_TOKEN", "value": "${SLACK_APP_TOKEN}"},
           {"name": "OPENAI_API_KEY", "value": "${OPENAI_API_KEY}"},
           {"name": "PINECONE_API_KEY", "value": "${PINECONE_API_KEY}"}
         ],
         "logConfiguration": {
           "logDriver": "awslogs",
           "options": {
             "awslogs-group": "/ecs/gutless-ai-assistant",
             "awslogs-region": "us-west-2",
             "awslogs-stream-prefix": "ecs"
           }
         }
       }
     ]
   }
   ```

3. **Create Service**:
   ```bash
   aws ecs create-service \
     --cluster gutless-ai-assistant \
     --service-name gutless-ai-assistant \
     --task-definition gutless-ai-assistant \
     --desired-count 1 \
     --launch-type FARGATE \
     --network-configuration "awsvpcConfiguration={subnets=[subnet-12345],securityGroups=[sg-12345],assignPublicIp=ENABLED}"
   ```

#### Option 2: AWS Lambda (Serverless)

1. **Install Serverless Framework**:
   ```bash
   npm install -g serverless
   ```

2. **Create `serverless.yml`**:
   ```yaml
   service: gutless-ai-assistant
   
   provider:
     name: aws
     runtime: python3.11
     region: us-west-2
     environment:
       SLACK_BOT_TOKEN: ${env:SLACK_BOT_TOKEN}
       SLACK_SIGNING_SECRET: ${env:SLACK_SIGNING_SECRET}
       OPENAI_API_KEY: ${env:OPENAI_API_KEY}
       PINECONE_API_KEY: ${env:PINECONE_API_KEY}
   
   functions:
     slack-bot:
       handler: src.lambda_handler.handler
       events:
         - http:
             path: slack/events
             method: post
   ```

### Google Cloud Deployment

#### Google Cloud Run

1. **Build and push image**:
   ```bash
   # Configure Docker for GCR
   gcloud auth configure-docker
   
   # Build and push
   docker build -t gcr.io/PROJECT-ID/gutless-ai-assistant .
   docker push gcr.io/PROJECT-ID/gutless-ai-assistant
   ```

2. **Deploy to Cloud Run**:
   ```bash
   gcloud run deploy gutless-ai-assistant \
     --image gcr.io/PROJECT-ID/gutless-ai-assistant \
     --platform managed \
     --region us-central1 \
     --set-env-vars SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN,SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET,SLACK_APP_TOKEN=$SLACK_APP_TOKEN,OPENAI_API_KEY=$OPENAI_API_KEY,PINECONE_API_KEY=$PINECONE_API_KEY
   ```

### Azure Deployment

#### Azure Container Instances

1. **Create resource group**:
   ```bash
   az group create --name gutless-ai-assistant --location eastus
   ```

2. **Deploy container**:
   ```bash
   az container create \
     --resource-group gutless-ai-assistant \
     --name gutless-ai-assistant \
     --image ghcr.io/your-username/gutless-ai-assistant:latest \
     --environment-variables \
       SLACK_BOT_TOKEN=$SLACK_BOT_TOKEN \
       SLACK_SIGNING_SECRET=$SLACK_SIGNING_SECRET \
       SLACK_APP_TOKEN=$SLACK_APP_TOKEN \
       OPENAI_API_KEY=$OPENAI_API_KEY \
       PINECONE_API_KEY=$PINECONE_API_KEY
   ```

### Heroku Deployment

1. **Install Heroku CLI** and login:
   ```bash
   heroku login
   ```

2. **Create Heroku app**:
   ```bash
   heroku create gutless-ai-assistant
   ```

3. **Set environment variables**:
   ```bash
   heroku config:set SLACK_BOT_TOKEN=your-token
   heroku config:set SLACK_SIGNING_SECRET=your-secret
   heroku config:set SLACK_APP_TOKEN=your-app-token
   heroku config:set OPENAI_API_KEY=your-openai-key
   heroku config:set PINECONE_API_KEY=your-pinecone-key
   heroku config:set PINECONE_ENVIRONMENT=us-west1-gcp
   heroku config:set PINECONE_INDEX_NAME=gutless-ai-assistant
   ```

4. **Deploy**:
   ```bash
   # Using Docker
   heroku container:push web
   heroku container:release web
   
   # Or using Git
   git push heroku main
   ```

## Kubernetes Deployment

### 1. Create Namespace

```yaml
# namespace.yaml
apiVersion: v1
kind: Namespace
metadata:
  name: gutless-ai-assistant
```

### 2. Create Secret

```yaml
# secret.yaml
apiVersion: v1
kind: Secret
metadata:
  name: gutless-ai-assistant-secrets
  namespace: gutless-ai-assistant
type: Opaque
stringData:
  SLACK_BOT_TOKEN: "xoxb-your-bot-token"
  SLACK_SIGNING_SECRET: "your-signing-secret"
  SLACK_APP_TOKEN: "xapp-your-app-token"
  OPENAI_API_KEY: "sk-your-openai-key"
  PINECONE_API_KEY: "your-pinecone-key"
  PINECONE_ENVIRONMENT: "us-west1-gcp"
  PINECONE_INDEX_NAME: "gutless-ai-assistant"
```

### 3. Create Deployment

```yaml
# deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: gutless-ai-assistant
  namespace: gutless-ai-assistant
spec:
  replicas: 1
  selector:
    matchLabels:
      app: gutless-ai-assistant
  template:
    metadata:
      labels:
        app: gutless-ai-assistant
    spec:
      containers:
      - name: gutless-ai-assistant
        image: ghcr.io/your-username/gutless-ai-assistant:latest
        envFrom:
        - secretRef:
            name: gutless-ai-assistant-secrets
        resources:
          requests:
            memory: "256Mi"
            cpu: "250m"
          limits:
            memory: "512Mi"
            cpu: "500m"
        livenessProbe:
          exec:
            command:
            - python
            - -c
            - "import sys; sys.exit(0)"
          initialDelaySeconds: 30
          periodSeconds: 30
        readinessProbe:
          exec:
            command:
            - python
            - -c
            - "import sys; sys.exit(0)"
          initialDelaySeconds: 5
          periodSeconds: 10
```

### 4. Deploy to Kubernetes

```bash
kubectl apply -f namespace.yaml
kubectl apply -f secret.yaml
kubectl apply -f deployment.yaml
```

## CI/CD with GitHub Actions

The repository includes a GitHub Actions workflow (`.github/workflows/deploy.yml`) that:

1. **Tests** the application
2. **Builds** and pushes Docker images
3. **Scans** for security vulnerabilities
4. **Deploys** to staging and production environments

### Setup GitHub Actions

1. **Configure secrets** in your GitHub repository:
   - `SLACK_BOT_TOKEN`
   - `SLACK_SIGNING_SECRET`
   - `SLACK_APP_TOKEN`
   - `OPENAI_API_KEY`
   - `PINECONE_API_KEY`
   - Cloud platform credentials (AWS, GCP, Azure)

2. **Customize deployment targets** in `.github/workflows/deploy.yml`

3. **Push to main branch** or create a tag to trigger deployment

## Monitoring and Logging

### Application Logs

```bash
# Docker Compose
docker-compose logs -f gutless-ai-assistant

# Kubernetes
kubectl logs -f deployment/gutless-ai-assistant -n gutless-ai-assistant

# AWS ECS
aws logs tail /ecs/gutless-ai-assistant --follow
```

### Health Checks

The application includes health check endpoints that can be used with:

- **Docker**: Built-in health checks
- **Kubernetes**: Liveness and readiness probes
- **Cloud platforms**: Load balancer health checks

### Monitoring Tools

- **Prometheus + Grafana**: For metrics collection and visualization
- **ELK Stack**: For centralized logging
- **Cloud monitoring**: AWS CloudWatch, Google Cloud Monitoring, Azure Monitor

## Troubleshooting

### Common Issues

1. **Environment Variables**: Ensure all required environment variables are set
2. **API Keys**: Verify API keys are valid and have proper permissions
3. **Network**: Check firewall rules and security groups
4. **Resources**: Monitor CPU and memory usage
5. **Dependencies**: Ensure external services (Pinecone, OpenAI) are accessible

### Debug Mode

Enable debug logging by setting:

```bash
LOG_LEVEL=DEBUG
DEVELOPMENT_MODE=true
```

### Support

For deployment issues:

1. Check the [troubleshooting guide](troubleshooting.md)
2. Review application logs
3. Verify configuration settings
4. Test API connectivity

## Security Considerations

1. **Secrets Management**: Use proper secret management services
2. **Network Security**: Implement proper firewall rules
3. **Image Security**: Regularly scan Docker images for vulnerabilities
4. **Access Control**: Use least privilege principles
5. **Monitoring**: Implement security monitoring and alerting

## Scaling

### Horizontal Scaling

- **Kubernetes**: Use Horizontal Pod Autoscaler (HPA)
- **Cloud platforms**: Configure auto-scaling groups
- **Load balancing**: Distribute traffic across multiple instances

### Vertical Scaling

- **Resource limits**: Adjust CPU and memory limits
- **Instance types**: Use appropriate instance sizes
- **Performance monitoring**: Monitor resource utilization

## Cost Optimization

1. **Right-sizing**: Use appropriate instance sizes
2. **Auto-scaling**: Scale down during low usage
3. **Reserved instances**: Use reserved instances for predictable workloads
4. **Spot instances**: Use spot instances for non-critical workloads
5. **Resource monitoring**: Monitor and optimize resource usage