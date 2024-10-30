# Merge Issue Overview CSV export for Vulnerabilities  

## Overview
This tool allows you to merge multiple CSV files containing FOSSA's Issue Overview Export for vulnerability data into a single CSV file. The script is capable of merging between 2 and 6 CSV files, combining the data while considering certain conditions for remediated and ignored vulnerabilities. 

## Features
- Merges between 2 to 6 CSV files.
- Retains the most relevant data in case of conflicting entries.
- Outputs a merged CSV file named `merged_vulnerabilities.csv`.

## Prerequisites
- Python 3.x

## Installation
Clone the repository or download the script to your local machine.

## Usage
To use the script, run the following command:

```bash
python merge_vulnerabilities.py <csv_file_1> <csv_file_2> [<csv_file_3> ... <csv_file_6>]
```

- `<csv_file_1>`, `<csv_file_2>`, etc.: Paths to the CSV files that you want to merge. You must provide at least 2 files, and you can provide up to 6 files.

### Example
```bash
python merge_vulnerabilities.py vulnerabilities_1.csv vulnerabilities_2.csv vulnerabilities_3.csv
```
This command will merge the data from `vulnerabilities_1.csv`, `vulnerabilities_2.csv`, and `vulnerabilities_3.csv` into a new file called `merged_vulnerabilities.csv`.

## Output
The merged CSV file will be saved in the current working directory with the name `merged_vulnerabilities.csv`.

## Logic Explanation
- The script loads each CSV file into a dictionary for processing.
- Each row is identified by a unique key consisting of `issueId` and `project`.
- If the same key exists in multiple files, the script keeps the entry that contains non-empty `remediatedAt` or `ignoredAt` fields, prioritizing the most relevant information.

## Error Handling
- The script requires at least 2 CSV files and will support up to 6 files.
- If incorrect usage is detected (less than 2 or more than 6 files), the script will display a usage message and terminate.

## Notes
- Ensure that the CSV files have consistent headers for proper merging.
- The output file will contain all combined data from the input files with the correct prioritization of fields.

## License
This project is licensed under the MIT License.
