#!/usr/bin/env python3

import json
import argparse
import yaml

def parse_arguments():
    parser = argparse.ArgumentParser(description='Generate fossa-deps.yml from Buildroot package info.')
    parser.add_argument('input_file', type=str, help='Path to the JSON file containing package information.')
    return parser.parse_args()

def load_package_info(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def map_to_fossa_type(package_name):
    # Define mapping rules from Buildroot packages to FOSSA dependency types
    if package_name.startswith('python-'):
        return 'pypi'
    elif package_name.startswith('ruby-'):
        return 'gem'
    else:
        return 'custom'

def transform_package_name(package_name):
    # Remove 'python-' if the package name starts with it
    if package_name.startswith('python-'):
        return package_name.replace('python-', '', 1)
    return package_name

def generate_fossa_deps(packages):
    referenced_deps = []
    custom_deps = []

    for pkg_name, pkg_info in packages.items():
        transformed_name = transform_package_name(pkg_name)  # Apply name transformation
        fossa_type = map_to_fossa_type(pkg_name)

        # Get version and ensure it is not empty or blank
        version = pkg_info.get('version', None)
        if not version or str(version).strip() == "":
            version = '1.0'  # Set default version if empty

        dep_entry = {
            'name': transformed_name,  # Use transformed package name
            'version': version
        }
        if fossa_type == 'custom':
            dep_entry['license'] = pkg_info.get('licenses', 'unknown')
            custom_deps.append(dep_entry)
        else:
            dep_entry['type'] = fossa_type
            referenced_deps.append(dep_entry)

    fossa_deps = {}
    if referenced_deps:
        fossa_deps['referenced-dependencies'] = referenced_deps
    if custom_deps:
        fossa_deps['custom-dependencies'] = custom_deps

    return fossa_deps

def main():
    args = parse_arguments()
    packages = load_package_info(args.input_file)
    fossa_deps = generate_fossa_deps(packages)

    with open('fossa-deps.yml', 'w') as f:
        yaml.dump(fossa_deps, f, default_flow_style=False)

    print('fossa-deps.yml has been generated.')

if __name__ == '__main__':
    main()
