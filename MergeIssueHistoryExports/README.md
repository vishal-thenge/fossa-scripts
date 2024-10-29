# Merged Issue History CSVs Script

This script merges two CSV files containing vulnerability data based on unique identifiers (`issueId` and `project`). If a record exists in both CSVs, it will be merged into 1 entyr. This also considers if the `remediatedAt` or `ignoredAt` fields have changed in one of the CSV files. The script will select the entry which has a non-empty `remediatedAt` or `ignoredAt` in the merged output.

## Requirements

- Python 3.x
- `csv` and `os` modules (included in standard Python library)
- `BeautifulSoup` library (`beautifulsoup4` package)

## Usage

### Command Line Usage

To use this script, run the following command:

```sh
python merge_vulnerabilities.py <csv_file_1> <csv_file_2>
