#  Task 154: Add log rotation when a file exceeds a fixed size.

import logging
from logging.handlers import RotatingFileHandler

def setup_rotating_logger(log_file="app.log"):
    logger = logging.getLogger("RotatingLogger")
    logger.setLevel(logging.INFO)

    # Rotate file when it reaches 1MB, keep 5 backups
    handler = RotatingFileHandler(log_file, maxBytes=1024 * 1024, backupCount=5)
    
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    
    logger.addHandler(handler)
    return logger

if __name__ == "__main__":
    logger = setup_rotating_logger()
    
    print("Writing to rotating log file...")
    for i in range(100):
        logger.info(f"Logging message number {i}")
        
    print("Check app.log to see the output.")

print(" \n Python 30 days Series - Day 21 : Task 154 \n"                                                 )
print(" \n Day 21 : Logging, Monitoring, and Alerts \n"                                                )
print(" \n Have a good one! \n "                          + "-"*40)
