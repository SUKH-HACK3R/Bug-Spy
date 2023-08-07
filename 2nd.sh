#!/bin/bash

# Save the current directory
current_dir=$(pwd)

# Move to a temporary directory
temp_dir=$(mktemp -d)
cd "$temp_dir" || exit

# Copy the .app.py script to a temporary file
cp "$current_dir/.app.py" script.py

# Run the temporary script
python3 script.py

# Clean up temporary files and return to the original directory
rm script.py
cd "$current_dir" || exit
rmdir "$temp_dir"
