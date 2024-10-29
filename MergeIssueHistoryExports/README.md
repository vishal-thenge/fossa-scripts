# Merged Vulnerabilities CSV Script

This script merges two CSV files containing vulnerability data based on unique identifiers (`issueId` and `project`). If a record exists in both CSVs, it will be merged only if the `remediatedAt` or `ignoredAt` fields have changed in one of the CSV files. The script will select the entry which has a non-empty `remediatedAt` or `ignoredAt` in the merged output.

## Requirements

- Python 3.x
- `csv` and `os` modules (included in standard Python library)
- `BeautifulSoup` library (`beautifulsoup4` package)

## Usage

### Command Line Usage

To use this script, run the following command:

```sh
python mergeIssueHistoryCSVs.py <csv_file_1> <csv_file_2>
<IssueHistoryExport_Month_1>: Path to the first CSV file.
<IssueHistoryExport_Month_2>: Path to the second CSV file.
The merged CSV file will be saved in the current working directory as merged_vulnerabilities.csv.



Copy code
python mergeIssueHistoryCSVs.py IssueHistoryExport_Month_1.csv IssueHistoryExport_Month_2.csv
This command will create a merged file called merged_vulnerabilities.csv in the current directory.

Script Overview
The script performs the following steps:

Load CSV Files: Loads the data from both input CSV files into a dictionary where each record is uniquely identified by a combination of issueId and project.

Merge Records: Compares records from different CSV files with the same key and merges them if the remediatedAt or ignoredAt fields differ between the two.

Write Merged Data: Writes the merged data into a new CSV file called merged_vulnerabilities.csv.

Logic for Merging Records
Records are uniquely identified by a combination of issueId and project.
Only records from different input CSV files are compared.
If the remediatedAt or ignoredAt fields differ between the two records, the entry with the non-empty value for these fields is retained.
Notes
The merged file will overwrite any existing file with the same name (merged_vulnerabilities.csv).
Ensure both input CSV files have issueId and project columns for proper identification and merging.
Error Handling
If the script does not receive exactly two arguments, it will display a usage message and exit.
The script will print an error message if it cannot read or write the specified files.
License
This script is provided as-is, without any warranty. You are free to use, modify, and distribute it as needed. """)

