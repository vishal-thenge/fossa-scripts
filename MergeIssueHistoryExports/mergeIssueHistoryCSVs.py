import csv
import sys
import os
from datetime import datetime

def merge_vulnerabilities(csv_file_1, csv_file_2):
    # Load CSV files into dictionaries
    data = {}

    def load_csv(file_path, source):
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                key = (row['issueId'], row['project'])
                if key not in data:
                    data[key] = {"row": row, "source": source}
                else:
                    # Only compare rows from different input CSVs
                    if data[key]["source"] != source:
                        existing_row = data[key]["row"]
                        if (existing_row.get('remediatedAt') != row.get('remediatedAt') or
                            existing_row.get('ignoredAt') != row.get('ignoredAt')):
                            # Use the entry with non-empty 'remediatedAt' or 'ignoredAt'
                            if row.get('remediatedAt') or row.get('ignoredAt'):
                                data[key]["row"] = row
                            elif not existing_row.get('remediatedAt') and not existing_row.get('ignoredAt'):
                                data[key]["row"] = row

    # Load data from both CSV files
    load_csv(csv_file_1, 'file1')
    load_csv(csv_file_2, 'file2')

    # Write merged data to output CSV
    output_file = os.path.join(os.getcwd(), 'merged_vulnerabilities.csv')
    if data:
        with open(output_file, 'w', newline='') as file:
            fieldnames = list(data[next(iter(data))]["row"].keys())
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for entry in data.values():
                writer.writerow(entry["row"])
        print(f"Merged CSV file saved to: {output_file}")
    else:
        print("No data to write.")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python mergeIssueHistoryCSVs.py <csv_file_1> <csv_file_2>")
        sys.exit(1)
    
    csv_file_1 = sys.argv[1]
    csv_file_2 = sys.argv[2]
    
    merge_vulnerabilities(csv_file_1, csv_file_2)

