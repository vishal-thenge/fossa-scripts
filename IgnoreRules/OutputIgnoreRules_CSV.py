import requests
import sys
import argparse

# Set up command line argument parsing
parser = argparse.ArgumentParser(description="Convert Ignore Rules into CSV")
parser.add_argument('scope', type=str, help='The scope to check (e.g., "ORGANIZATION")')
parser.add_argument('category', type=str, help='Category can be licensing or security')
parser.add_argument('token', type=str, help='The FOSSA API key')

args = parser.parse_args()


# Main function
def main(token, depSubString):
    url = 'https://app.fossa.com/api/v2/issues/exceptions'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }
    params = {
        'filters[category]': args.category,
        'category': args.category,
        'ignoreScope': args.scope
    }
    data = { }

    # Sending GET request
    response = requests.get(url, headers=headers, params=params, json=data)

    if response.status_code == 200:
        print("Request successful.")
        json_response = response.json()
        # Iterate through response to fetch ids
        for issue in json_response['exceptions']:
            issue_id = issue['id']
            issue_title = issue['exceptionTitle']
            issue_note = issue['note']
            issue_dep_locator = issue['dependencyProjectLocator']
            scope = issue['ignoreScope']
            #print(f"Found Ignore Issue: {issue_note}: {issue_title} : {scope}; Dependency:{issue_dep_locator}" )
    else:
        print(f"Request failed with status code {response.status_code}.")

# Execute main function
if __name__ == "__main__":
   main(args.token, args.dependency)          
