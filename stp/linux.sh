#!/bin/bash
cd "$(dirname $(dirname $(realpath "$0")))"

checkmark=$"\e[92m\u2713\e[0m"
cross=$"\e[31m\u2717\e[0m"

success() {
    echo -e "[${checkmark}]: $1"
}

failure() {
    echo -e "[${cross}]: $1\n[\e[31mSETUP FAILED\e[0m]"
    exit 1
}

if [[ "$(uname)" != "Linux" ]]; then
    failure "This script must run on Linux."
fi

reqCmd() {
    if command -v $1 > /dev/null 2>&1; then
        success "Command '$1' was found."
    else
        failure "Command '$1' was NOT found. '$1' is a dependency."
    fi
}

reqCmd docker

echo -e "[\e[92mSETUP SUCCEEDED\e[0m]"