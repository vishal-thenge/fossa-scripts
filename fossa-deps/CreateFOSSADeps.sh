#!/bin/bash

# Initialize the fossa-deps.yaml file
output_file="fossa-deps.yaml"
echo "vendored-dependencies:" > "$output_file"

# Find all RPM files recursively from the current directory
find . -type f -name "*.rpm" | while read -r rpm_file; do
    # Extract the version using rpm -qp
    version=$(rpm -qp --queryformat '%{VERSION}\n' "$rpm_file" 2>/dev/null)
    
    # Check if the version was successfully retrieved
    if [[ -n "$version" ]]; then
        # Get the RPM file name without the path
        rpm_name=$(basename "$rpm_file" .rpm)
        
        # Format the relative path to the RPM file
        #relative_path=$(realpath --relative-to="$(pwd)" "$rpm_file")
        relative_path=$(python3 -c "import os; print(os.path.relpath('$rpm_file', '$base_dir'))")

        absolute_path=$(realpath "$rpm_file")
        
        # Append the dependency information to fossa-deps.yaml
        echo "- name: ${rpm_name}" >> "$output_file"
        echo "  path: ${relative_path}" >> "$output_file"
        #echo "  path: ${absolute_path}" >> "$output_file"
        echo "  version: ${version}" >> "$output_file"
    else
        echo "Error processing $rpm_file. Skipping." >&2
    fi
done

echo "fossa-deps.yaml has been generated successfully!"
