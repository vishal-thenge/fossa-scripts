
# RPM Dependency Scanner

This script scans a directory for RPM files, extracts their version information, and generates a `fossa-deps.yaml` file with details about the RPM name, path, and version.

## Features

- Recursively searches for RPM files starting from the current directory.
- Extracts the version of each RPM using `rpm -qp`.
- Computes relative paths for each RPM file.
- Outputs the results in a `fossa-deps.yaml` file in the following format:

```yaml
vendored-dependencies:
- name: <rpm-name>
  path: <relative-path-to-rpm>
  version: <rpm-version>
```

## Requirements

- **Bash**: Ensure you have a Bash shell environment.
- **Python 3**: Required to compute relative paths.
- **rpm**: The `rpm` command must be installed and accessible.
  
## How to Use

1. Save the script as `generate_fossa_deps.sh`.
2. Make the script executable:
   ```bash
   chmod +x generate_fossa_deps.sh
   ```
3. Run the script in the directory containing your RPM files:
   ```bash
   ./generate_fossa_deps.sh
   ```
4. The script will create a `fossa-deps.yaml` file in the current directory.

## Example Output

For a directory structure like this:
```
/project/
├── bin/
│   └── bash-5.2.37-15.1.i586.rpm
├── lib/
│   └── libfoo-1.2.3-4.x86_64.rpm
```

The generated `fossa-deps.yaml` will look like:
```yaml
vendored-dependencies:
- name: bash-5.2.37-15.1.i586
  path: bin/bash-5.2.37-15.1.i586.rpm
  version: 5.2.37
- name: libfoo-1.2.3-4.x86_64
  path: lib/libfoo-1.2.3-4.x86_64.rpm
  version: 1.2.3
```

## Troubleshooting

- If you encounter errors while running the script:
  - Ensure `rpm` is installed and functional.
  - Verify that the script has execute permissions (`chmod +x`).
  - Check for Python 3 installation (`python3 --version`).

## License

This script is provided under the MIT License. Feel free to use and modify it as needed.
