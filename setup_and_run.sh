#!/bin/bash

################################################################################
# NUVIEW Strategic Pipeline - Setup and Run Script
# 
# This script automates the setup and execution of the NUVIEW Strategic Pipeline
# - Clones the repository if not present
# - Pulls latest updates from GitHub
# - Sets up Python virtual environment if needed
# - Installs dependencies (if any)
# - Optionally runs the main pipeline scripts
#
# Usage: ./setup_and_run.sh [--run-pipeline]
#   --run-pipeline: Run scrape_all.py and qc_validator.py after update
#
# Compatible with: macOS (tested on macOS 10.15+)
################################################################################

set -e  # Exit on error

# Configuration
REPO_URL="https://github.com/JacobThielNUVIEW/nuview-strategic-pipeline.git"
# Allow override via environment variable, default to specified path
INSTALL_DIR="${NUVIEW_INSTALL_DIR:-$HOME/Documents/NUVIEW_Pipeline_tool}"
REPO_NAME="nuview-strategic-pipeline"
REPO_PATH="${INSTALL_DIR}/${REPO_NAME}"
VENV_NAME="venv"
VENV_PATH="${REPO_PATH}/${VENV_NAME}"

# Color codes for output
COLOR_GREEN='\033[0;32m'
COLOR_BLUE='\033[0;34m'
COLOR_YELLOW='\033[1;33m'
COLOR_RED='\033[0;31m'
COLOR_RESET='\033[0m'

# Parse command line arguments
RUN_PIPELINE=false
if [[ "$1" == "--run-pipeline" ]]; then
    RUN_PIPELINE=true
fi

################################################################################
# Helper Functions
################################################################################

print_header() {
    echo ""
    echo -e "${COLOR_BLUE}========================================${COLOR_RESET}"
    echo -e "${COLOR_BLUE}$1${COLOR_RESET}"
    echo -e "${COLOR_BLUE}========================================${COLOR_RESET}"
}

print_info() {
    echo -e "${COLOR_BLUE}ℹ️  $1${COLOR_RESET}"
}

print_success() {
    echo -e "${COLOR_GREEN}✅ $1${COLOR_RESET}"
}

print_warning() {
    echo -e "${COLOR_YELLOW}⚠️  $1${COLOR_RESET}"
}

print_error() {
    echo -e "${COLOR_RED}❌ $1${COLOR_RESET}"
}

################################################################################
# Main Setup Process
################################################################################

print_header "NUVIEW Strategic Pipeline - Setup & Update"

# Step 1: Check and create installation directory
print_info "Checking installation directory..."
if [ ! -d "$INSTALL_DIR" ]; then
    print_info "Creating installation directory: $INSTALL_DIR"
    mkdir -p "$INSTALL_DIR"
    print_success "Installation directory created"
else
    print_success "Installation directory exists"
fi

# Step 2: Clone or update repository
cd "$INSTALL_DIR"

if [ ! -d "$REPO_PATH" ]; then
    print_header "Cloning Repository"
    print_info "Cloning from: $REPO_URL"
    print_info "Destination: $REPO_PATH"
    
    if git clone "$REPO_URL"; then
        print_success "Repository cloned successfully"
    else
        print_error "Failed to clone repository"
        exit 1
    fi
else
    print_header "Updating Repository"
    cd "$REPO_PATH"
    
    print_info "Fetching latest changes..."
    if git fetch origin; then
        print_success "Fetched latest changes"
    else
        print_warning "Failed to fetch changes (continuing anyway)"
    fi
    
    # Check current branch
    CURRENT_BRANCH=$(git rev-parse --abbrev-ref HEAD)
    print_info "Current branch: $CURRENT_BRANCH"
    
    # Check for local changes
    STASH_CREATED=false
    if ! git diff-index --quiet HEAD --; then
        print_warning "Local changes detected in repository"
        print_warning "Stashing local changes before pulling..."
        STASH_MESSAGE="Auto-stash before update $(date '+%Y-%m-%d %H:%M:%S')"
        git stash push -m "$STASH_MESSAGE"
        STASH_CREATED=true
    fi
    
    # Pull latest changes
    print_info "Pulling latest changes..."
    if git pull origin "$CURRENT_BRANCH"; then
        print_success "Repository updated successfully"
    else
        print_warning "Failed to pull changes (you may need to resolve conflicts manually)"
    fi
    
    # Apply stashed changes if we created a stash
    if [ "$STASH_CREATED" = true ]; then
        print_info "Re-applying stashed changes..."
        git stash pop || print_warning "Could not re-apply stashed changes automatically"
    fi
fi

# Step 3: Setup Python virtual environment
cd "$REPO_PATH"
print_header "Python Virtual Environment Setup"

# Check for Python 3
if ! command -v python3 &> /dev/null; then
    print_error "Python 3 is not installed or not in PATH"
    print_error "Please install Python 3.8+ from https://www.python.org/downloads/"
    exit 1
fi

PYTHON_VERSION=$(python3 --version)
print_info "Found: $PYTHON_VERSION"

if [ ! -d "$VENV_PATH" ]; then
    print_info "Creating virtual environment..."
    if python3 -m venv "$VENV_NAME"; then
        print_success "Virtual environment created"
    else
        print_error "Failed to create virtual environment"
        exit 1
    fi
else
    print_success "Virtual environment already exists"
fi

# Activate virtual environment
print_info "Activating virtual environment..."
source "${VENV_PATH}/bin/activate"
print_success "Virtual environment activated"

# Step 4: Install/Update dependencies
print_header "Installing Dependencies"

if [ -f "requirements.txt" ]; then
    # Check if requirements.txt has actual dependencies
    if grep -q "^[^#]" requirements.txt; then
        print_info "Installing packages from requirements.txt..."
        if pip install --upgrade --quiet pip; then
            print_success "pip upgraded"
        fi
        
        if pip install -r requirements.txt; then
            print_success "Dependencies installed"
        else
            print_warning "Some dependencies failed to install"
        fi
    else
        print_info "No external dependencies required (using Python standard library)"
        print_success "All dependencies satisfied"
    fi
else
    print_warning "requirements.txt not found"
    print_info "Assuming no external dependencies needed"
fi

# Step 5: Verify installation
print_header "Verifying Installation"

MAIN_SCRIPT="scripts/scrapers/scrape_all.py"
VALIDATOR_SCRIPT="scripts/qc_validator.py"

if [ -f "$MAIN_SCRIPT" ]; then
    print_success "Main scraper script found: $MAIN_SCRIPT"
else
    print_error "Main scraper script not found: $MAIN_SCRIPT"
fi

if [ -f "$VALIDATOR_SCRIPT" ]; then
    print_success "QC validator script found: $VALIDATOR_SCRIPT"
else
    print_error "QC validator script not found: $VALIDATOR_SCRIPT"
fi

# Step 6: Run pipeline scripts (optional)
if [ "$RUN_PIPELINE" = true ]; then
    print_header "Running Pipeline Scripts"
    
    print_info "Running data scraper..."
    if python3 "$MAIN_SCRIPT"; then
        print_success "Scraper completed successfully"
    else
        print_error "Scraper failed"
        exit 1
    fi
    
    echo ""
    print_info "Running QC validator..."
    if python3 "$VALIDATOR_SCRIPT"; then
        print_success "QC validation passed"
    else
        print_error "QC validation failed"
        exit 1
    fi
    
    print_header "Pipeline Execution Complete"
    print_success "All pipeline scripts executed successfully"
    print_info "Data files have been updated:"
    print_info "  - data/opportunities.json"
    print_info "  - data/forecast.json"
    print_info "  - data/processed/qc_report.json"
else
    print_header "Setup Complete"
    print_success "Repository is ready to use"
    print_info ""
    print_info "To run the pipeline manually:"
    print_info "  1. Activate venv: source ${VENV_PATH}/bin/activate"
    print_info "  2. Run scraper: python3 ${MAIN_SCRIPT}"
    print_info "  3. Run validator: python3 ${VALIDATOR_SCRIPT}"
    print_info ""
    print_info "Or run this script with --run-pipeline flag:"
    print_info "  ./setup_and_run.sh --run-pipeline"
fi

print_header "Summary"
print_success "Repository location: $REPO_PATH"
print_success "Virtual environment: $VENV_PATH"
print_success "Status: Ready"

echo ""
