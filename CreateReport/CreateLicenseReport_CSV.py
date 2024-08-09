import requests
import csv
import argparse
import urllib.parse
import json

# Set up argument parsing
parser = argparse.ArgumentParser(description='Fetch report from FOSSA API, save to CSV.')
parser.add_argument('token', type=str, help='Authorization token for the FOSSA API')
parser.add_argument('json_file', type=str, help='Path to the JSON file created bg fossa analyze --json 1> output.json')

# Parse the input arguments
args = parser.parse_args()
TOKEN = args.token
json_file_path = args.json_file


# Load and parse the JSON file
with open(json_file_path, 'r') as json_file:
   parsed_json = json.load(json_file)
    
# Extract and URL encode the 'id' field
id_value = parsed_json['id']
encoded_id_value = urllib.parse.quote(id_value, safe='')
REVISION_ID=encoded_id_value

# API URL
API_URL = f'https://app.fossa.com/api/matches/?revisionId={REVISION_ID}'

# Headers
headers = {
    'Authorization': f'Bearer {TOKEN}'
}

try:
    # Make the API call
    response = requests.get(API_URL, headers=headers)
    
    # Check if the API call was successful
    if response.status_code != 200:
        raise requests.exceptions.RequestException(f"API call failed with status code {response.status_code}: {response.text}")

    # Parse the JSON response
    data = response.json()

    # Check if the response contains the 'matches' key
    if 'matches' not in data:
        raise ValueError("The response does not contain the 'matches' key.")

    # Open a CSV file for writing
    with open('LicenseReport_withFileMatches.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        
        # Write the header row
        writer.writerow([
            'id', 'path', 'signature', 'licenseId', 'copyrights', 'ignored', 
            'revisionLicenseId', 'sources', 'extractedLicenseText', 'revisionId', 
            'matchIdentityHash', 'createdAt', 'revisionLicense_id', 
            'revisionLicense_revisionId', 'revisionLicense_licenseId', 
            'revisionLicense_licenseGroupId', 'revision_locator', 
            'revision_projectId', 'project_locator', 'project_organizationId', 
            'project_public'
        ])
        
        # Write the data rows
        for match in data['matches']:
            writer.writerow([
                match.get('id'),
                match.get('path'),
                match.get('signature'),
                match.get('licenseId'),
                match.get('copyrights'),
                match.get('ignored'),
                match.get('revisionLicenseId'),
                ', '.join(match.get('sources', [])),
                match.get('extractedLicenseText'),
                match.get('revisionId'),
                match.get('matchIdentityHash'),
                match.get('createdAt'),
                match['RevisionLicense'].get('id'),
                match['RevisionLicense'].get('revisionId'),
                match['RevisionLicense'].get('licenseId'),
                match['RevisionLicense'].get('licenseGroupId'),
                match['RevisionLicense']['revision'].get('locator'),
                match['RevisionLicense']['revision'].get('projectId'),
                match['RevisionLicense']['revision']['project'].get('locator'),
                match['RevisionLicense']['revision']['project'].get('organizationId'),
                match['RevisionLicense']['revision']['project'].get('public')
            ])

    print("Data has been written to LicenseReport_withFileMatches.csv")

except requests.exceptions.RequestException as e:
    print(f"An error occurred while making the API request: {e}")
except ValueError as e:
    print(f"An error occurred with the API response: {e}")
except json.JSONDecodeError as e:
    print(f"An error occurred while parsing the JSON file: {e}")
except FileNotFoundError as e:
    print(f"The specified JSON file was not found: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
