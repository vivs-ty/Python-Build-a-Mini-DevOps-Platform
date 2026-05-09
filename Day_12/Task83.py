# Task 83: Build a CLI log analyzer that filters by log level.

# Task 83: Master Version
import argparse
from pathlib import Path

def main() -> None:
    parser = argparse.ArgumentParser(description="Filter logs by severity level.")
    
    parser.add_argument("logfile", type=str, help="Path to the log file")
    parser.add_argument(
        "-l", "--level", 
        choices=["INFO", "WARNING", "ERROR", "DEBUG"], 
        default="ERROR",
        help="The log level to filter by (default: ERROR)"
    )

    args = parser.parse_args()
    log_path = Path(args.logfile)

    if not log_path.exists():
        print(f"❌ Log file '{args.logfile}' not found.")
        return

    print(f"📊 Showing '{args.level}' logs from {log_path.name}:")
    with open(log_path, "r", encoding="utf-8") as f:
        matches = [line.strip() for line in f if f" {args.level} " in line]
        
    if matches:
        print("\n".join(matches))
    else:
        print(f"No {args.level} entries found.")

if __name__ == "__main__":
    main()

