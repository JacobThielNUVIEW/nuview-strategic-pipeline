# NUVIEW Strategic Pipeline - Setup Script

This document describes how to use the automated setup and run script for the NUVIEW Strategic Pipeline.

## Overview

The `setup_and_run.sh` script is a ready-to-run shell script that automates the complete setup and update workflow for the NUVIEW Strategic Pipeline. It is designed to be safe to run multiple times and is compatible with macOS.

## Features

- ✅ **Automatic Repository Management**: Clones the repository if not present, or pulls latest updates if it exists
- ✅ **Smart Update Handling**: Stashes local changes before pulling and re-applies them afterwards
- ✅ **Python Virtual Environment**: Creates and manages a Python virtual environment automatically
- ✅ **Dependency Management**: Installs or updates Python dependencies as needed
- ✅ **Optional Pipeline Execution**: Can automatically run the main pipeline scripts after update
- ✅ **Idempotent**: Safe to run multiple times without side effects
- ✅ **Clear Status Messages**: Provides colored output with progress indicators
- ✅ **macOS Compatible**: Tested and optimized for macOS environments

## Installation

The script will automatically install to: `$HOME/Documents/NUVIEW_Pipeline_tool/` (typically `/Users/JThiel/Documents/NUVIEW_Pipeline_tool/`)

### Custom Installation Directory

You can customize the installation directory by setting the `NUVIEW_INSTALL_DIR` environment variable:

```bash
export NUVIEW_INSTALL_DIR="/path/to/your/directory"
./setup_and_run.sh
```

Or inline:

```bash
NUVIEW_INSTALL_DIR="/path/to/your/directory" ./setup_and_run.sh
```

### Initial Setup

1. Download the script to your desired location (or run it directly from the repository):
   ```bash
   curl -O https://raw.githubusercontent.com/JacobThielNUVIEW/nuview-strategic-pipeline/main/setup_and_run.sh
   chmod +x setup_and_run.sh
   ```

2. Run the script for the first time:
   ```bash
   ./setup_and_run.sh
   ```

This will:
- Create the installation directory if it doesn't exist
- Clone the repository
- Set up a Python virtual environment
- Install any required dependencies

## Usage

### Basic Usage (Update Only)

To update the repository and dependencies without running the pipeline:

```bash
./setup_and_run.sh
```

This will:
- Pull the latest changes from GitHub
- Update the Python virtual environment if needed
- Install/update dependencies
- Display the status and manual run instructions

### Run with Pipeline Execution

To update AND run the main pipeline scripts automatically:

```bash
./setup_and_run.sh --run-pipeline
```

This will:
- Pull the latest changes from GitHub
- Update the virtual environment and dependencies
- Run `scripts/scrapers/scrape_all.py` to collect data
- Run `scripts/qc_validator.py` to validate the data
- Display the results and updated file locations

### Manual Pipeline Execution

If you prefer to run the pipeline scripts manually:

1. Navigate to the repository:
   ```bash
   cd /Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline
   ```

2. Activate the virtual environment:
   ```bash
   source venv/bin/activate
   ```

3. Run the scraper:
   ```bash
   python3 scripts/scrapers/scrape_all.py
   ```

4. Run the validator:
   ```bash
   python3 scripts/qc_validator.py
   ```

## What the Script Does

### Step-by-Step Process

1. **Installation Directory Check**
   - Verifies `/Users/JThiel/Documents/NUVIEW_Pipeline_tool` exists
   - Creates the directory if needed

2. **Repository Management**
   - **First Run**: Clones the repository from GitHub
   - **Subsequent Runs**: 
     - Fetches latest changes
     - Stashes any local modifications
     - Pulls updates from the current branch
     - Re-applies stashed changes

3. **Python Virtual Environment**
   - Checks for Python 3 installation
   - Creates a virtual environment if not present
   - Activates the virtual environment

4. **Dependency Installation**
   - Upgrades pip to the latest version
   - Installs packages from `requirements.txt`
   - Handles cases where no external dependencies are needed

5. **Verification**
   - Confirms all required scripts are present
   - Displays status of the installation

6. **Optional Pipeline Execution** (with `--run-pipeline` flag)
   - Runs the data scraper to update opportunities and forecast data
   - Runs the QC validator to ensure data quality
   - Reports success/failure of each step

## Prerequisites

- **macOS**: 10.15 (Catalina) or later
- **Python**: 3.8 or higher (3.10+ recommended)
- **Git**: Pre-installed on macOS or available via Xcode Command Line Tools
- **Internet Connection**: Required for cloning/pulling repository

To install Xcode Command Line Tools (if git is not available):
```bash
xcode-select --install
```

## Output Files

When the pipeline runs (with `--run-pipeline` flag), it generates/updates:

- `data/opportunities.json` - Current opportunity pipeline data
- `data/forecast.json` - Market forecast data
- `data/processed/qc_report.json` - Quality control validation report

## Troubleshooting

### Python Not Found
```
❌ Python 3 is not installed or not in PATH
```
**Solution**: Install Python 3 from [python.org](https://www.python.org/downloads/) or via Homebrew:
```bash
brew install python3
```

### Git Clone Failed
```
❌ Failed to clone repository
```
**Solution**: Check your internet connection and verify you have access to the repository.

### Local Changes Detected
```
⚠️ Local changes detected in repository
⚠️ Stashing local changes before pulling...
```
**Note**: This is normal behavior. The script automatically stashes your changes, pulls updates, and attempts to re-apply your changes. If there are conflicts, you may need to resolve them manually.

### QC Validation Failed
```
❌ QC validation failed
```
**Solution**: Review the `data/processed/qc_report.json` file for details about what failed validation. The report contains specific error messages and warnings.

## Scheduling Automatic Updates

### Using cron (macOS)

To run the script automatically, you can set up a cron job:

1. Open crontab editor:
   ```bash
   crontab -e
   ```

2. Add a line to run daily at 3 AM:
   ```
   0 3 * * * /Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline/setup_and_run.sh --run-pipeline >> /Users/JThiel/Documents/NUVIEW_Pipeline_tool/update.log 2>&1
   ```

3. Save and exit

### Using launchd (macOS - Preferred)

For a more robust macOS solution, you can create a Launch Agent:

1. Create a plist file at `~/Library/LaunchAgents/com.nuview.pipeline.update.plist`:
   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
   <plist version="1.0">
   <dict>
       <key>Label</key>
       <string>com.nuview.pipeline.update</string>
       <key>ProgramArguments</key>
       <array>
           <string>/Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline/setup_and_run.sh</string>
           <string>--run-pipeline</string>
       </array>
       <key>StartCalendarInterval</key>
       <dict>
           <key>Hour</key>
           <integer>3</integer>
           <key>Minute</key>
           <integer>0</integer>
       </dict>
       <key>StandardOutPath</key>
       <string>/Users/JThiel/Documents/NUVIEW_Pipeline_tool/update.log</string>
       <key>StandardErrorPath</key>
       <string>/Users/JThiel/Documents/NUVIEW_Pipeline_tool/update_error.log</string>
   </dict>
   </plist>
   ```

2. Load the Launch Agent:
   ```bash
   launchctl load ~/Library/LaunchAgents/com.nuview.pipeline.update.plist
   ```

3. To unload (stop automatic updates):
   ```bash
   launchctl unload ~/Library/LaunchAgents/com.nuview.pipeline.update.plist
   ```

## Security Notes

- The script uses HTTPS for git operations (no credentials stored)
- No sensitive data is transmitted or stored by the script
- Virtual environment isolates Python dependencies
- All operations are performed in the user's home directory

## Script Location

The script can be placed anywhere, but for convenience, you might want to:

1. **Keep it in the repository** (recommended):
   ```bash
   cd /Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline
   ./setup_and_run.sh --run-pipeline
   ```

2. **Create a symlink** for easy access:
   ```bash
   ln -s /Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline/setup_and_run.sh ~/bin/nuview-update
   nuview-update --run-pipeline
   ```

3. **Add to PATH** by adding to `~/.zshrc` or `~/.bash_profile`:
   ```bash
   export PATH="/Users/JThiel/Documents/NUVIEW_Pipeline_tool/nuview-strategic-pipeline:$PATH"
   ```

## Support

For issues or questions:
- Review the troubleshooting section above
- Check the main repository README.md for general information
- Review the script output for specific error messages

## License

Proprietary - NUVIEW Space Technologies, Inc.
