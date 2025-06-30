#!/bin/bash
cd "$(dirname $(dirname $(realpath "$0")))"

if [[ "$(uname)" != "Linux" ]]; then
    echo -e "Error: This script must be run on Linux.\nEXITING..."
    exit 1
fi

reqCmd() {
    if ! command -v $1 > /dev/null 2>&1; then
        echo -e "Command '$1' was not found. '$1' is a dependency.\nEXITING..."
        exit 1
    fi
}

reqCmd python3
reqCmd clang++