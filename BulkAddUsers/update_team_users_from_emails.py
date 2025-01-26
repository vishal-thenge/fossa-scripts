import requests
import csv
import sys

# API Base URL
base_url = "https://app.fossa.com/api"

# Fetch all users and map email to user ID
def fetch_user_id_map(api_token):
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    try:
        response = requests.get(f"{base_url}/users?count=12000", headers=headers)
        if response.status_code == 200:
            users = response.json()
            # Create a dictionary mapping email to user ID
            print("Response:", response.text)
            return {user["email"]: user["id"] for user in users}
        else:
            print(f"Failed to fetch users. Status: {response.status_code}")
            return {}
    except Exception as e:
        print(f"Error fetching users: {e}")
        return {}

# Read CSV and make API calls
def update_team_users_from_csv(file_path, api_token):
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_token}"
    }

    # Fetch the user ID map once
    user_id_map = fetch_user_id_map(api_token)
  
    if not user_id_map:
        print("No users found. Aborting operation.")
        return

    try:
        with open(file_path, mode='r') as csv_file:
            reader = csv.DictReader(csv_file)

            for row in reader:
                team_id = row['teamId']
                role_id = int(row['roleId'])
                email = row['email']

                # Get user ID from the map
                user_id = user_id_map.get(email)
                if not user_id:
                    print(f"User with email '{email}' not found in FOSSA.")
                    continue

                # Construct the API endpoint and body
                endpoint = f"{base_url}/teams/{team_id}/users"
                data = {
                    "users": [{"id": user_id, "roleId": role_id}],
                    "action": "add"
                }

                # Make the PUT request
                try:
                    response = requests.put(endpoint, json=data, headers=headers)
                    print(f"JSON: {data}")
                    if response.status_code == 200:
                        print(f"Success: User {email} added to Team {team_id}.")
                    else:
                        print(f"Failed: Team {team_id}, User {email}. Status: {response.status_code}")
                except Exception as e:
                    print(f"Error adding user {email} to Team {team_id}: {e}")

    except FileNotFoundError:
        print(f"Error: The file {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Main function
if __name__ == "__main__":
    # Check for required arguments
    if len(sys.argv) != 3:
        print("Usage: python update_team_users_from_emails.py <CSV_FILE_PATH> <API_TOKEN>")
        sys.exit(1)

    # Get arguments
    csv_file_path = sys.argv[1]
    api_token = sys.argv[2]

    # Call the function
    update_team_users_from_csv(csv_file_path, api_token)
                      
