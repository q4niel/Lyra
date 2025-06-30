#!/bin/bash
cd "$(dirname $(dirname $(dirname $(dirname $(realpath "$0")))))"
source "bld/run/linux/util.sh"
runPy bld/src/build.py