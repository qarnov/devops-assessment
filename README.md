# DevOps Assessment: Log Monitoring Script

This project is a solution for a DevOps assessment task to create a script that automates the analysis and monitoring of log files.

## Requirements
- Python 3 should be installed on your system:
  - For Linux: `sudo apt install python3 python3-pip`
  - For Windows: [Download Python 3](https://www.python.org/downloads/windows/)

## Usage
To use this project, follow these steps:
1. Clone the repository.
2. Change the `"error.log"` in the script to match the name of your log file. For example, if your log file is named `"error.log"`, leave it as is.
3. Make sure the log file is in the same directory as the script.
4. Run the script using the command: `python3 log-monitor.py`

The script continuously monitors the log file and provides insights into common WordPress errors. It also includes a mechanism to stop the monitoring loop:
- **Automated Timeout:** If there is no activity for 30 seconds, the script will automatically stop. This prevents misuse of computing power.
- **Manual Interruption:** Pressing `Ctrl+C` will raise a `KeyboardInterrupt` and stop the script. This is useful for manually stopping the script during long-running operations.

## Log Monitoring Features
The script is optimized for monitoring WordPress error log files. It includes solutions for common WordPress issues sorted by keywords:
1. **Fatal Error:** Check your WordPress plugins. Try disabling them one by one to identify the problematic plugin.
2. **wp-settings:** Try upgrading/downgrading your PHP version.
3. **403 Error:** Rename your `.htaccess` file.
4. **elementor:** Look into `public_html/wp-content/plugins/elementor/includes/settings` on the 76th line.
5. **wp-content/themes:** Try changing the theme to the default one and check.

The script also counts the occurrences of each error type, allowing users to identify patterns in their website's issues.

## Logging Module
The `logging` module in Python was used for the following reasons:
- **Error Logging:** Provides structured logging of error messages and possible solutions.
- **Level-Based Logging:** Different log levels (INFO, WARNING, ERROR) for different types of messages.
- **Standardized Output:** Logs messages with timestamps, log levels, and actual log messages for readability.
- **Flexibility:** Logs can be output to console, files, or other destinations.
- **Debugging and Maintenance:** Helps in debugging and maintaining the script by providing a clear record of script activities.
