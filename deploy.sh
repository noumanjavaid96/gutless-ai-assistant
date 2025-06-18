#!/bin/bash

# Renesis AI Assistant Deployment Script
# This script helps deploy the Slack bot application

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Function to check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."
    
    if ! command_exists docker; then
        print_error "Docker is not installed. Please install Docker first."
        exit 1
    fi
    
    if ! command_exists docker-compose; then
        print_error "Docker Compose is not installed. Please install Docker Compose first."
        exit 1
    fi
    
    print_success "Prerequisites check passed!"
}

# Function to setup environment
setup_environment() {
    print_status "Setting up environment..."
    
    if [ ! -f ".env" ]; then
        if [ -f ".env.example" ]; then
            cp .env.example .env
            print_warning "Created .env file from .env.example. Please update it with your actual values."
        else
            print_error ".env.example file not found. Please create a .env file with required environment variables."
            exit 1
        fi
    else
        print_success ".env file already exists."
    fi
}

# Function to build the application
build_application() {
    print_status "Building the application..."
    docker-compose build
    print_success "Application built successfully!"
}

# Function to start the application
start_application() {
    print_status "Starting the application..."
    docker-compose up -d
    print_success "Application started successfully!"
    
    print_status "Checking application status..."
    sleep 5
    docker-compose ps
}

# Function to stop the application
stop_application() {
    print_status "Stopping the application..."
    docker-compose down
    print_success "Application stopped successfully!"
}

# Function to show logs
show_logs() {
    print_status "Showing application logs..."
    docker-compose logs -f gutless-ai-assistant
}

# Function to show status
show_status() {
    print_status "Application status:"
    docker-compose ps
    
    print_status "\nApplication logs (last 20 lines):"
    docker-compose logs --tail=20 gutless-ai-assistant
}

# Function to restart the application
restart_application() {
    print_status "Restarting the application..."
    docker-compose restart
    print_success "Application restarted successfully!"
}

# Function to update the application
update_application() {
    print_status "Updating the application..."
    git pull origin main
    docker-compose build
    docker-compose up -d
    print_success "Application updated successfully!"
}

# Function to show help
show_help() {
    echo "Renesis AI Assistant Deployment Script"
    echo ""
    echo "Usage: $0 [COMMAND]"
    echo ""
    echo "Commands:"
    echo "  setup     - Setup environment and build application"
    echo "  start     - Start the application"
    echo "  stop      - Stop the application"
    echo "  restart   - Restart the application"
    echo "  status    - Show application status and logs"
    echo "  logs      - Show live application logs"
    echo "  update    - Update and restart the application"
    echo "  help      - Show this help message"
    echo ""
    echo "Examples:"
    echo "  $0 setup     # Initial setup"
    echo "  $0 start     # Start the bot"
    echo "  $0 logs      # View live logs"
}

# Main script logic
case "${1:-}" in
    setup)
        check_prerequisites
        setup_environment
        build_application
        print_success "Setup completed! Run '$0 start' to start the application."
        ;;
    start)
        check_prerequisites
        start_application
        ;;
    stop)
        stop_application
        ;;
    restart)
        restart_application
        ;;
    status)
        show_status
        ;;
    logs)
        show_logs
        ;;
    update)
        update_application
        ;;
    help|--help|-h)
        show_help
        ;;
    "")
        print_error "No command specified."
        show_help
        exit 1
        ;;
    *)
        print_error "Unknown command: $1"
        show_help
        exit 1
        ;;
esac