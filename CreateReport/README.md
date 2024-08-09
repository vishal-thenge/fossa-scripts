
# Create a FOSSA License report CSV

## Description

This script creates a License report including the License file matches and stores it in a CSV file. This uses the API to fetch data from the FOSSA API and saves it to a CSV file. It requires an authorization token and a JSON file created by the fossa analyze --json 1> output.json to function.

## Usage

### Prerequisites

- Python 3.x
- `requests` library

You can install the `requests` library using pip:

```sh
pip install requests
```

### Running the Script


Arguments needed:
  token       Authorization token for the FOSSA API
  json_file   Path to the JSON file created bg fossa analyze --json 1> output.json

### Example

```sh
python CreateLicenseReport_CSV.py <your_api_token_here> <path to the JSON file created by fossa analyze>
```

### Output

The script will generate a `LicenseReport_withFileMatches.csv` file containing the data from the API response.


## License

This project is licensed under the MIT License.
