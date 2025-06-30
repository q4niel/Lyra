#!/bin/bash

runPy() {
    if [[ "$(uname)" != "Linux" ]]; then
        echo -e "This script must run on Linux!"
        exit 1
    fi

    if ! [ -d "bld/venv" ]; then
        python3 -m venv bld/venv
        source bld/venv/bin/activate
        pip install lupa
    else
        source bld/venv/bin/activate
    fi

    python3 -B $1
    deactivate
}