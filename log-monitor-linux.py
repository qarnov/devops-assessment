import subprocess
import logging
import time
from collections import defaultdict

# Setup logging
logging.basicConfig(level=logging.INFO)
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

    # Command to execute 'tail -f' on the log file
    tail_command = ["tail", "-f", log_file]

    start_time = time.time()

    try:
        # Open a subprocess to execute the 'tail -f' command
        with subprocess.Popen(tail_command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True) as process:
            # Read the output of the command line by line
            for line in process.stdout:
                # Process each line as needed
                logger.info("Latest log entry:")
                logger.info(line.strip())  # Log the line
                analyze_log_line(line)  # Analyze the log entry

                # Print the total count of each error type
                logger.info("\nNumber of times each error has occurred:")
                for error_type, count in error_counts.items():
                    logger.info(f"{error_type}: {count}")

                # Check for timeout every 30 minutes = 1800 seconds
                if time.time() - start_time >= 1800:
                    logger.warning("No new error found after the last scan. Hence stopped the script.")
                    break  # Stop monitoring after 30 minutes = 1800 seconds

    except KeyboardInterrupt:
        logger.info("\nMonitoring stopped by user.")

def main():
    log_file = "error.log"  # Assuming the error log file is in the same directory

    # Count errors in the entire log file
    logger.info(f"Analyzing log file: {log_file}")
    monitor_log_file(log_file)

if __name__ == "__main__":
    main()
