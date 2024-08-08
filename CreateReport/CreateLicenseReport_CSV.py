import requests
import csv
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Fetch data from FOSSA API and save to CSV.')
parser.add_argument('token', type=str, help='Authorization token for the FOSSA API')
parser.add_argument('revision_id', type=str, help='Revision ID for the FOSSA API')

# Parse the input arguments
args = parser.parse_args()
TOKEN = args.token
REVISION_ID = args.revision_id

# API URL
API_URL = f'https://app.fossa.com/api/matches/?revisionId={REVISION_ID}'

# Headers
headers = {
    'Authorization': f'Bearer {TOKEN}'
}

# Make the API call
response = requests.get(API_URL, headers=headers)
data = response.json()

# Open a CSV file for writing
with open('LicenseReport.csv', mode='w', newline='') as file:
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

print("Data has been written to LicenseReport.csv")
