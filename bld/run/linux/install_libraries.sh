#!/bin/bash
cd "$(dirname $(dirname $(dirname $(dirname $(realpath "$0")))))"
source "bld/run/linux/util.sh"
runDocker bld/src/install_libraries.py
copyDocker "3rd" "3rd"