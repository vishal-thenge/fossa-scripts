# Buildroot to FOSSA Dependency Converter

This script extracts package information from a **Buildroot JSON output** (`make show-info`) and converts it into a `fossa-deps.yml` file for **FOSSA license and security analysis**.

## Features
- Reads **Buildroot package JSON** (`make show-info > package_info.json`).
- Removes the prefix **`python-`** from package names.
- If a package **has no version**, it defaults to **`1.0`**.
- Categorizes dependencies into:
  - `referenced-dependencies` (e.g., **pypi**, **gem**).
  - `custom-dependencies` (if not in a known package manager).

## Requirements
- Python 3.x
- Buildroot (`make show-info` must be available)
- `PyYAML` package (install using `pip install pyyaml`)

## Installation
1. Clone or download the script:
   ```bash
   git clone https://github.com/your-repo/buildroot-fossa-converter.git
   cd buildroot-fossa-converter
   ```

2. Ensure you have the necessary Python dependencies:
   ```bash
   pip install pyyaml
   ```

3. Make the script executable:
   ```bash
   chmod +x generate_fossa_deps.py
   ```

## Usage
### 1. Generate Buildroot JSON:
Run the following command inside your Buildroot environment:
```bash
make show-info > package_info.json
```
This will create a `package_info.json` file containing metadata about all enabled Buildroot packages.

### 2. Convert JSON to `fossa-deps.yml`:
Run the script:
```bash
./generate_fossa_deps.py package_info.json
```
This will generate a `fossa-deps.yml` file.

## Example Output
### **Input (`package_info.json`):**
```json
{
  "python-requests": {
    "version": "",
    "licenses": "Apache-2.0"
  },
  "busybox": {
    "version": "1.35.0",
    "licenses": "GPL-2.0"
  },
  "python-numpy": {
    "version": "1.21.2",
    "licenses": "BSD-3-Clause"
  }
}
```

### **Generated `fossa-deps.yml`:**
```yaml
referenced-dependencies:
  - name: requests
    version: '1.0'
    type: pypi
  - name: numpy
    version: 1.21.2
    type: pypi
custom-dependencies:
  - name: busybox
    version: 1.35.0
    license: GPL-2.0
```

## Notes
- **Packages prefixed with `python-` have the prefix removed** (e.g., `python-requests` → `requests`).
- **Empty versions are replaced with `'1.0'`**.
- Dependencies **are categorized based on package type**.

## License
MIT License
