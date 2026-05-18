#  Task 153: Design a custom logging system with timestamps and log levels.

import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
def log_message(level, message):
    if level == 'info':
        logging.info(message)
    elif level == 'warning':
        logging.warning(message)
    elif level == 'error':
        logging.error(message)
    print(f"[{time.strftime('%Y-%m-%d %H:%M:%S')}] {level.upper()}: {message}")
if __name__ == "__main__":
    log_message('info', 'This is an informational message.')
    log_message('warning', 'This is a warning message.')
    log_message('error', 'This is an error message.')
    