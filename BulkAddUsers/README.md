# `update_team_users_from_emails.py`

## Overview

`update_team_users_from_emails.py` is a Python script designed to streamline the process of adding users to FOSSA teams by leveraging their email addresses. The script retrieves user IDs via the FOSSA API, matches them to the corresponding emails from a CSV file, and assigns them to the specified teams with the designated roles.

---

## Features

- **Bulk Add Users**: Automates adding multiple users to teams using data from a CSV file.
- **FOSSA API Integration**: Retrieves user IDs dynamically from the FOSSA API based on email addresses.
- **Custom Roles**: Allows specifying roles for each user in the CSV file.
- **Error Handling**: Provides detailed feedback for missing users or API errors.

---

## Requirements

- Python 3.7 or later
- Required Python libraries:
  - `requests`

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/vishal-thenge/fossa-scripts.git
   cd fossa-scripts/BulkAddUsers
   ```

2. **Install Dependencies**:
   ```bash
   pip install requests
   ```

---

## Usage

1. **Prepare the CSV File**:
   Create a CSV file (e.g., `team_user_emails.csv`) with the following structure:

   ```csv
   teamId,email,roleId
   57272,user1@example.com,6
   57273,user2@example.com,5
   57274,user3@example.com,6
   ```

   - `teamId`: ID of the team in FOSSA.
   - `email`: User's email address.
   - `roleId`: Role ID to assign to the user.

2. **Run the Script**:
   Execute the script with the CSV file path and your FOSSA API token:
   ```bash
   python update_team_users_from_emails.py team_user_emails.csv <API_TOKEN>
   ```

3. **Example Command**:
   ```bash
   python update_team_users_from_emails.py team_user_emails.csv abc123xyz456
   ```

---

## Notes

- The script makes a single call to the FOSSA API to fetch all users, ensuring efficient handling of bulk operations.
- If a user email from the CSV file is not found, the script will log a message and skip the entry.

---

## License

This script is provided under the MIT License. See the repository's `LICENSE` file for more details.
