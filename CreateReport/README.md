
# FOSSA API to CSV Script

## Description

This script fetches data from the FOSSA API and saves it to a CSV file. It requires an authorization token and a revision ID to function.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```

### Running the Script



Replace `<your_api_token_here>` with your actual API token and `<your_revision_id_here>` with the desired revision ID.

### Example

```sh
python CreateLicenseReport_CSV.py <your_api_token_here> <your_revision_id_here>
```

### Output

The script will generate a `LicenseReport.csv` file containing the data from the API response.


## License

This project is licensed under the MIT License.
