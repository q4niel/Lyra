#!/bin/bash
cd "$(dirname $(realpath "$0"))"

# Find the first executable file that matches ./bin/lyra*
lyra=$(find ./bin -maxdepth 1 -type f -executable -name 'lyra*' | head -n 1)

# Check if a matching binary was found
if [[ -z "$lyra" ]]; then
    echo "Error: No matching executable found for './bin/lyra*'"
    exit 1
fi

# Run Lyra with custom linker and local libs
./bin/ld-linux-x86-64.so.2 --library-path ./bin "$lyra" "$@"