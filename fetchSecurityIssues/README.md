
# FOSSA Security Issues Fetcher

This script is designed to fetch security issues from the FOSSA API based on the severity level. It uses the provided FOSSA API token, project identifier, and project revision identifier to retrieve and save the security issues.

## Prerequisites

- Python 3.x
- `requests` library

You can install the required library using pip:

```bash
pip install requests

```

## Usage

The script can be run from the command line with the following arguments:

- `token`: FOSSA API token.
- `severity`: Severity level of issues to fetch. Choices are `critical`, `high`, `medium`, and `low`.
- `project`: Project identifier.
- `revision`: Project revision identifier.

### Example Command

```bash
python fetchSecurityIssues.py --token YOUR_FOSSA_API_TOKEN --severity high --project YOUR_PROJECT_ID --revision YOUR_PROJECT_REVISION
```

### Arguments

- `--token`: Your FOSSA API token. This is required to authenticate and access the FOSSA API.
- `--severity`: The severity level of the issues you want to fetch. Options are `critical`, `high`, `medium`, `low`.
- `--project`: The identifier of the project for which you want to fetch issues.
- `--revision`: The revision identifier of the project.

## Output

The script will save the fetched issues filtered by the specified severity to a JSON file named `<severity>_issues.json`. For example, if the severity is `high`, the output file will be `high_issues.json`.

## Example Output

If you run the script with the following command:

```bash
python fetchSecurityIssues.py --token abc123 --severity high --project my_project --revision 1.0.0
```

And there are issues with high severity, the script will save them to a file named `high_issues.json` in the same directory.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
