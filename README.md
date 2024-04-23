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
Results trying it in  windows system(Click link to view the screenshot):https://snipboard.io/hbZq4J.jpg
https://snipboard.io/bkAcOe.jpg

Results trying it in Linux system(Click link to view the screenshot):https://snipboard.io/pZPvJc.jpg 
https://snipboard.io/0x3KGa.jpg

## Log Monitoring Features
As at my first job, I had to assist customer's with their wordpress website errors, I have decided to optimize the script for monitoring wordpress error logs file just to see if I could make customer's lives easy by giving them automated reports fetched from their wordpress error log files.
I have included 4 of the most common wordpress issues me and my team used to get that is are sorted by keywords:
1. **Fatal Error:** Check your WordPress plugins. Try disabling them one by one to identify the problematic plugin.
2. **wp-settings:** Try upgrading/downgrading your PHP version.
3. **403 Error:** Rename your `.htaccess` file.
4. **elementor:** Look into `public_html/wp-content/plugins/elementor/includes/settings` on the 76th line.
5. **wp-content/themes:** Try changing the theme to the default one and check.


So when the script summarises the issue, it wil prompt the user to do the following.The script also counts the occurrences of each error type, allowing users to identify patterns in their website's issues.

## Log Analyzing features
The `logging` module in Python was used for the following reasons:
- **Error Logging:** Provides structured logging of error messages and possible solutions.
- **Level-Based Logging:** The logging module provides different levels of logging (DEBUG, INFO, WARNING, ERROR, CRITICAL), which allows for different types of messages to be logged. In this script, we are using different log levels for different types of messages:
INFO level for general information messages.
WARNING level for warnings about no new log entries or script termination.
ERROR level for reporting errors such as the log file not being found.
- **Standardized Output:** By using logging, the script can output log messages in a standardized format, which includes a timestamp, log level, and the actual log message. This makes it easier to read and understand the log messages.
- **Flexibility:** The logging module provides flexibility in where the logs are sent. In this script, the logs are sent to the console, but it can be configured to log to files, email, or other destinations without changing the script logic.
- **Debugging and Maintenance:** Implementing logging helps in debugging the script and maintaining it in the long run. It provides a clear record of what the script is doing, what errors it encounters, and how it responds to different situations.

# Additonal Features

- **Automated Timeout:** The script includes a timeout mechanism that automatically stops the monitoring if there is no activity for 30 seconds. This prevents unnecessary resource consumption.
- **Manual Interruption:** Users can manually stop the script by pressing Ctrl+C, which raises a KeyboardInterrupt. This provides a convenient way to halt the script during execution.
- **Error Logging with Logging Module:** The script utilizes the logging module in Python to log error messages, information, and warnings. This provides structured and organized logging of errors and solutions.
- **Level-Based Logging:** Different log levels are used for different types of messages:
  - **INFO level:** General information messages.
  - **WARNING level:** Warnings about no new log entries or script termination.
  - **ERROR level:** Reporting errors such as the log file not being found.
- **Standardized Output:** By using the logging module, the script outputs log messages in a standardized format, including a timestamp, log level, and the actual log message. This improves readability and understanding of the logs.
- **Error Counting:** The script counts the occurrences of each error type, such as "elementor," "403," "fatal error," "wp-settings," and "wp-content/themes." Users can identify patterns in their website's issues based on these counts.
- **Providing Solutions:** For each detected error type, the script provides a possible solution. For example:
  - "Possible Solution: Check the wp-content/plugins/elementor/includes/settings and then check its 76th line and comment it"
  - "Possible Solution: Rename .htaccess"
  - "Possible Solution: Check your WordPress plugins. Try disabling them one by one to check which causes problems."
  - "Possible Solution: Try upgrading/downgrading your PHP version."
  - "Possible Solution: Try changing the theme to the default one and check."
- **Tail-like Functionality (Linux):** A separate script named "log-monitor-linux.py" has been optimized for Linux systems. This script uses the tail command similar to the Unix command-line tool to display the last part of a file.


# Future Possible Features

- **Implement an Email Notification System:** To alert the user/administrator when specific errors occur or when certain thresholds are reached. Since we already included the logging module, this implementation is already half done.
  
- **Machine Learning for Anomaly Detection:** Utilize machine learning algorithms to detect anomalies in log data. This could help identify unusual patterns or outliers that may indicate potential issues.
  
- **Customizable Reporting:** Allow users to generate customized reports based on selected time ranges, error types, or other criteria. Reports could be exported in various formats such as PDF or CSV.


