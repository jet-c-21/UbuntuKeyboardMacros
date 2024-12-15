#!/bin/bash

# Debug flag: Set to true to enable debug logs, false to disable
DEBUG=false

# Ensure the script uses the correct Python environment
PYTHON_BIN=~/miniconda3/bin/python3

# Path to your Python script
PYTHON_SCRIPT=~/my_home/UbuntuKeyboardMacros/py_scripts/move_window_to_right_monitor.py

# Log file path (only define when DEBUG is true)
if [ "$DEBUG" = true ]; then
    LOG_FILE=~/my_home/UbuntuKeyboardMacros/logs/move_window_to_right_monitor.log
    # Create the logs directory if it doesn't exist
    mkdir -p ~/my_home/UbuntuKeyboardMacros/logs
else
    LOG_FILE=/dev/null  # Discard logs when DEBUG is false
fi

# Function to log debug messages
log_debug() {
    if [ "$DEBUG" = true ]; then
        echo "$(date '+%Y-%m-%d %H:%M:%S'): $1" >> "$LOG_FILE"
    fi
}

# Log the start of the script
log_debug "Starting move_window_to_right_monitor script"

# Run the Python script and log its output
$PYTHON_BIN "$PYTHON_SCRIPT" >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

# Log the success or failure of the Python script execution
if [ "$EXIT_CODE" -eq 0 ]; then
    log_debug "Python script executed successfully"
else
    log_debug "Python script execution failed with exit code $EXIT_CODE"
fi

# Log the end of the script
log_debug "Finished move_window_to_right_monitor script"
