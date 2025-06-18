# Renesis AI Assistant Deployment Script for Windows
# This PowerShell script helps deploy the Slack bot application on Windows

param(
    [Parameter(Position=0)]
    [ValidateSet('setup', 'start', 'stop', 'restart', 'status', 'logs', 'update', 'help')]
    [string]$Command = 'help'
)

# Function to print colored output
function Write-Status {
    param([string]$Message)
    Write-Host "[INFO] $Message" -ForegroundColor Blue
}

function Write-Success {
    param([string]$Message)
    Write-Host "[SUCCESS] $Message" -ForegroundColor Green
}

function Write-Warning {
    param([string]$Message)
    Write-Host "[WARNING] $Message" -ForegroundColor Yellow
}

function Write-Error {
    param([string]$Message)
    Write-Host "[ERROR] $Message" -ForegroundColor Red
}

# Function to check if command exists
function Test-CommandExists {
    param([string]$Command)
    $null -ne (Get-Command $Command -ErrorAction SilentlyContinue)
}

# Function to check prerequisites
function Test-Prerequisites {
    Write-Status "Checking prerequisites..."
    
    if (-not (Test-CommandExists "docker")) {
        Write-Error "Docker is not installed. Please install Docker Desktop first."
        exit 1
    }
    
    if (-not (Test-CommandExists "docker-compose")) {
        Write-Error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    }
    
    Write-Success "Prerequisites check passed!"
}

# Function to setup environment
function Initialize-Environment {
    Write-Status "Setting up environment..."
    
    if (-not (Test-Path ".env")) {
        if (Test-Path ".env.example") {
            Copy-Item ".env.example" ".env"
            Write-Warning "Created .env file from .env.example. Please update it with your actual values."
        } else {
            Write-Error ".env.example file not found. Please create a .env file with required environment variables."
            exit 1
        }
    } else {
        Write-Success ".env file already exists."
    }
}

# Function to build the application
function Build-Application {
    Write-Status "Building the application..."
    docker-compose build
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Application built successfully!"
    } else {
        Write-Error "Failed to build application."
        exit 1
    }
}

# Function to start the application
function Start-Application {
    Write-Status "Starting the application..."
    docker-compose up -d
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Application started successfully!"
        
        Write-Status "Checking application status..."
        Start-Sleep -Seconds 5
        docker-compose ps
    } else {
        Write-Error "Failed to start application."
        exit 1
    }
}

# Function to stop the application
function Stop-Application {
    Write-Status "Stopping the application..."
    docker-compose down
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Application stopped successfully!"
    } else {
        Write-Error "Failed to stop application."
        exit 1
    }
}

# Function to show logs
function Show-Logs {
    Write-Status "Showing application logs..."
    docker-compose logs -f gutless-ai-assistant
}

# Function to show status
function Show-Status {
    Write-Status "Application status:"
    docker-compose ps
    
    Write-Status "`nApplication logs (last 20 lines):"
    docker-compose logs --tail=20 gutless-ai-assistant
}

# Function to restart the application
function Restart-Application {
    Write-Status "Restarting the application..."
    docker-compose restart
    if ($LASTEXITCODE -eq 0) {
        Write-Success "Application restarted successfully!"
    } else {
        Write-Error "Failed to restart application."
        exit 1
    }
}

# Function to update the application
function Update-Application {
    Write-Status "Updating the application..."
    git pull origin main
    if ($LASTEXITCODE -eq 0) {
        docker-compose build
        if ($LASTEXITCODE -eq 0) {
            docker-compose up -d
            if ($LASTEXITCODE -eq 0) {
                Write-Success "Application updated successfully!"
            } else {
                Write-Error "Failed to start updated application."
                exit 1
            }
        } else {
            Write-Error "Failed to build updated application."
            exit 1
        }
    } else {
        Write-Error "Failed to pull latest changes."
        exit 1
    }
}

# Function to show help
function Show-Help {
    Write-Host "Renesis AI Assistant Deployment Script for Windows" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Usage: .\deploy.ps1 [COMMAND]" -ForegroundColor White
    Write-Host ""
    Write-Host "Commands:" -ForegroundColor White
    Write-Host "  setup     - Setup environment and build application" -ForegroundColor Gray
    Write-Host "  start     - Start the application" -ForegroundColor Gray
    Write-Host "  stop      - Stop the application" -ForegroundColor Gray
    Write-Host "  restart   - Restart the application" -ForegroundColor Gray
    Write-Host "  status    - Show application status and logs" -ForegroundColor Gray
    Write-Host "  logs      - Show live application logs" -ForegroundColor Gray
    Write-Host "  update    - Update and restart the application" -ForegroundColor Gray
    Write-Host "  help      - Show this help message" -ForegroundColor Gray
    Write-Host ""
    Write-Host "Examples:" -ForegroundColor White
    Write-Host "  .\deploy.ps1 setup     # Initial setup" -ForegroundColor Gray
    Write-Host "  .\deploy.ps1 start     # Start the bot" -ForegroundColor Gray
    Write-Host "  .\deploy.ps1 logs      # View live logs" -ForegroundColor Gray
}

# Main script logic
switch ($Command) {
    'setup' {
        Test-Prerequisites
        Initialize-Environment
        Build-Application
        Write-Success "Setup completed! Run '.\deploy.ps1 start' to start the application."
    }
    'start' {
        Test-Prerequisites
        Start-Application
    }
    'stop' {
        Stop-Application
    }
    'restart' {
        Restart-Application
    }
    'status' {
        Show-Status
    }
    'logs' {
        Show-Logs
    }
    'update' {
        Update-Application
    }
    'help' {
        Show-Help
    }
    default {
        Write-Error "Unknown command: $Command"
        Show-Help
        exit 1
    }
}