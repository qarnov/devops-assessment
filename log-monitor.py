import os
import time
import logging
from collections import defaultdict

# Setup logging with timestamps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Dictionary to store the count of each error type
error_counts = defaultdict(int)

def analyze_log_line(line):
    global error_counts

    # Convert line to lowercase for case-insensitive matching
    line_lower = line.lower()

    if "elementor" in line_lower:
        error_counts["elementor"] += 1
        logger.info("Possible Solution: Check the wp-content/plugins/elementor/includes/settings and then check its 76th line and comment it")
    elif "403" in line_lower:
        error_counts["403"] += 1
        logger.info(f"Possible Solution: Rename .htaccess\nNumber of times this error has occurred: {error_counts['403']}")
    elif "fatal error" in line_lower:
        error_counts["fatal_error"] += 1
        logger.info("Possible Solution: Check your WordPress plugins. Try disabling them one by one to check which causes problems.")
    elif "wp-settings" in line_lower:
        error_counts["wp_settings"] += 1
        logger.info("Possible Solution: Try upgrading/downgrading your PHP version.")
    elif "wp-content/themes" in line_lower:
        error_counts["wp_themes"] += 1
        logger.info("Possible Solution: Try changing the theme to the default one and check.")
    # Add more conditions for other keywords as needed
    else:
        logger.info("Sorry, script cannot help with this log entry")

def monitor_log_file(log_file):
    global error_counts

    # Check if log file exists
    if not os.path.exists(log_file):
        logger.error(f"Error: Log file '{log_file}' not found.")
        return

    start_time = time.time()
    last_scan_time = start_time

    # Variables to track warnings
    no_new_entry_warning_shown = False
    log_file_name_warning_shown = False

    # Open the log file in read mode
    with open(log_file, 'r') as file:
        file.seek(0, os.SEEK_END)  # Go to the end of the file
        try:
            while True:
                line = file.readline()
                if line:
                    logger.info("Latest log entry:")
                    logger.info(line.strip())  # Print the latest log entry
                    analyze_log_line(line)  # Analyze the log entry
                    last_scan_time = time.time()  # Update last scan time

                    # Print the total count of each error type
                    logger.info("\nNumber of times each error has occurred:")
                    for error_type, count in error_counts.items():
                        logger.info(f"{error_type}: {count}")

                    # Reset the warning flag since new log entry is found
                    no_new_entry_warning_shown = False

                # Check if 30 minutes=1800 seconds have passed since the script started
                if time.time() - start_time >= 1800 and not log_file_name_warning_shown:
                    logger.warning("No new error found after the last scan. Hence stopped the script.")
                    log_file_name_warning_shown = True
                    break  # Stop monitoring after 30 minutes = 1800 seconds

                time.sleep(0.1)  # Sleep for a short duration
                file.seek(file.tell())  # Move to the current end of the file
        except KeyboardInterrupt:
            logger.info("\nMonitoring stopped by user.")

def main():
    log_file = "error.log"  # Assuming the error log file is in the same directory

    # Count errors in the entire log file
    logger.info(f"Analyzing log file: {log_file}")
    monitor_log_file(log_file)

if __name__ == "__main__":
    main()
