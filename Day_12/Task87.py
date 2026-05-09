# Task 87: Support flags like --verbose and --dry-run.

# Task 87: Master Version
import argparse
import logging
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Safe File Deleter")
    
    parser.add_argument("target", help="File to delete")
    
    # action="store_true" means if the flag is present, it's True. Otherwise False.
    parser.add_argument("-v", "--verbose", action="store_true", help="Enable detailed logging")
    parser.add_argument("--dry-run", action="store_true", help="Simulate without deleting")

    args = parser.parse_args()

    # Set up logging based on verbosity
    log_level = logging.DEBUG if args.verbose else logging.INFO
    logging.basicConfig(level=log_level, format="%(levelname)s: %(message)s")

    target_path = Path(args.target)
    
    logging.debug(f"Target path resolved to: {target_path.absolute()}")

    if args.dry_run:
        logging.info(f"🛡️ DRY RUN: Would have deleted '{target_path.name}'")
    else:
        if target_path.exists():
            target_path.unlink() # Actual deletion
            logging.info(f"✅ DELETED: '{target_path.name}'")
        else:
            logging.error(f"❌ File '{target_path.name}' not found.")

if __name__ == "__main__":
    main()

