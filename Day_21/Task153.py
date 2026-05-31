#  Task 153: Design a custom logging system with timestamps and log levels.

import logging

def setup_custom_logger():
    # Create a custom logger
    logger = logging.getLogger("SystemLogger")
    logger.setLevel(logging.DEBUG)

    # Create console handler
    console_handler = logging.StreamHandler()
    
    # Create a formatter with timestamps
    formatter = logging.Formatter('[%(asctime)s] %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
    console_handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(console_handler)
    return logger

if __name__ == "__main__":
    log = setup_custom_logger()
    
    log.info("This is an informational message.")
    log.warning("This is a warning message.")
    log.error("This is an error message.")
    log.debug("This is a debug message.")

print(" \n Python 30 days Series - Day 21 : Task 153 \n"                                                 )
print(" \n Day 21 : Logging, Monitoring, and Alerts \n"                                                )
print(" \n Have a good one! \n "                          + "-"*40)
