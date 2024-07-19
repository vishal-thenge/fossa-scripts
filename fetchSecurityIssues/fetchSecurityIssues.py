import requests
import json
import argparse

def fetch_fossa_issues(token, severity, project, revision):
    # Define the API endpoint and headers
    url = f'https://app.fossa.com/api/v2/issues?category=vulnerability&scope%5Btype%5D=project&scope%5Bid%5D={project}&scope%5Brevision%5D={revision}'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token}'
    }

    # Define the data payload
    data = {
        "depth?": "direct",
        "severity?": severity,
        "scope?": "project",
        "csv": "true"
    }

    # Make the GET request
    response = requests.get(url, headers=headers, json=data)

    # Check the response status code and handle the response accordingly
    if response.status_code == 200:
        print("Success!")
        response_data = response.json()

        # Assuming 'issues' key contains the list of issue dictionaries
        issues = response_data.get('issues', [])

        # Filter issues by the specified severity
        filtered_issues = [issue for issue in issues if issue.get("severity") == severity]

        # Save filtered issues to a separate JSON file
        filename = f'{severity}_issues.json'
        with open(filename, 'w') as f:
            json.dump(filtered_issues, f, indent=4)

        print(f"{severity.capitalize()} issues have been saved to {filename}")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch FOSSA issues by severity.')
    parser.add_argument('token', type=str, help='FOSSA API token')
    parser.add_argument('severity', type=str, choices=['critical', 'high', 'medium', 'low'], help='Severity level of issues to fetch')
    parser.add_argument('project', type=str, help='Project identifier')
    parser.add_argument('revision', type=str, help='Project revision identifier')

    args = parser.parse_args()
    
    fetch_fossa_issues(args.token, args.severity, args.project, args.revision)

