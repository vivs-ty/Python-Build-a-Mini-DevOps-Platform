# Task 117: Process multiple CSV files in parallel and calculate aggregated statistics.

import concurrent.futures
import csv
from pathlib import Path

# Setup dummy CSVs
Path("sales_jan.csv").write_text("item,revenue\nA,100\nB,250")
Path("sales_feb.csv").write_text("item,revenue\nA,150\nB,300\nC,50")

def process_csv(file_path: Path) -> dict:
    """Worker: Calculates total revenue and row count for a single CSV."""
    total_rev = 0.0
    row_count = 0
    with open(file_path, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for row in reader:
            total_rev += float(row["revenue"])
            row_count += 1
    return {"file": file_path.name, "revenue": total_rev, "rows": row_count}

def main() -> None:
    csv_files = [Path("sales_jan.csv"), Path("sales_feb.csv")]
    
    total_revenue = 0.0
    total_rows = 0

    print(" Processing CSV files in parallel...")
    with concurrent.futures.ProcessPoolExecutor() as executor:
        for result in executor.map(process_csv, csv_files):
            print(f"  -> {result['file']} processed: ${result['revenue']} across {result['rows']} rows.")
            total_revenue += result['revenue']
            total_rows += result['rows']
            
    print("-" * 40)
    print(f" Grand Total Revenue: ${total_revenue:.2f}")
    print(f" Global Average:      ${total_revenue / total_rows:.2f} per item")

if __name__ == "__main__":
    main()
    print(f" \n Python 30 days Series - Day 16 Task 117 \n")
    print(f" \n Day 16 : Multiprocessing \n")
    print(f" \n Have a good one! \n " + "-"*40)
    