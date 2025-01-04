#!/bin/bash

# Change directory to the location of this script
cd "$(dirname "$0")"

# Find all Python files in the current directory and run them
for script in *.py; do
    echo "Running $script..."
    python "$script" || { echo "Test failed: $script"; exit 1; }
done

echo "All tests completed successfully."