#  Task 154: Add log rotation when a file exceeds a fixed size.

import logging
import os
from logging.handlers import RotatingFileHandler

# Set up the rotating file handler
log_file = "app.log"
max_bytes = 1024 * 1024  # 1 MB
backup_count = 5

handler = RotatingFileHandler(log_file, maxBytes=max_bytes, backupCount=backup_count)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Set up the logger
logger = logging.getLogger(__name__)
logger.addHandler(handler)
logger.setLevel(logging.INFO)
if __name__ == "__main__":
    for i in range(10000):
        logger.info(f"Logging message number {i}")
        