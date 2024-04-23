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
- **Using tail module:** In the provided code, we did not use the tail module of Python. The tail module is not a built-in Python module; it's a common Unix command-line tool used to display the last part of a file. In the script, we manually implemented a similar functionality by opening the log file and continuously reading new lines from the end of the file (`file.seek(0, os.SEEK_END)`) as new entries are appended. This way, we mimic the behavior of tail in a Python script without actually using the tail module. However, since there was a requirement mentioned in the assessment to "Use tail or similar commands to track and display new log entries in real time," I decided to implement tail in another code file optimized for Linux systems. This file is named "log-monitor-linux.py." Since I personally use Windows, I can use "log-monitor-linux.py" when using my VPS server where I host client websites.

## Log Monitoring Features
As at my first job, I had to assist customer's with their wordpress website errors, I have decided to optimize the script for monitoring wordpress error logs file just to see if I could make customer's lives easy by giving them automated reports fetched from their wordpress error log files.
I have included 4 of the most common wordpress issues me and my team used to get that is are sorted by keywords:
1. **Fatal Error:** Check your WordPress plugins. Try disabling them one by one to identify the problematic plugin.
2. **wp-settings:** Try upgrading/downgrading your PHP version.
3. **403 Error:** Rename your `.htaccess` file.
4. **elementor:** Look into `public_html/wp-content/plugins/elementor/includes/settings` on the 76th line.
5. **wp-content/themes:** Try changing the theme to the default one and check.

The script also counts the occurrences of each error type, allowing users to identify patterns in their website's issues.

## Logging Module
The `logging` module in Python was used for the following reasons:
- **Error Logging:** Provides structured logging of error messages and possible solutions.
- **Level-Based Logging:** The logging module provides different levels of logging (DEBUG, INFO, WARNING, ERROR, CRITICAL), which allows for different types of messages to be logged. In this script, we are using different log levels for different types of messages:
INFO level for general information messages.
WARNING level for warnings about no new log entries or script termination.
ERROR level for reporting errors such as the log file not being found.
- **Standardized Output:** By using logging, the script can output log messages in a standardized format, which includes a timestamp, log level, and the actual log message. This makes it easier to read and understand the log messages.
- **Flexibility:** The logging module provides flexibility in where the logs are sent. In this script, the logs are sent to the console, but it can be configured to log to files, email, or other destinations without changing the script logic.
- **Debugging and Maintenance:** Implementing logging helps in debugging the script and maintaining it in the long run. It provides a clear record of what the script is doing, what errors it encounters, and how it responds to different situations.
