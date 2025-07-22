#!/bin/bash
cd "$(dirname $(dirname $(dirname $(dirname $(realpath "$0")))))"
source "bld/run/linux/util.sh"
runDocker bld/src/build.py
if [ ! -d bld/out ]; then
    mkdir bld/out
fi
copyDocker "bld/out" "bld/out"
sudo mv "bld/out/out" "bld/out/$(date +"%Y_%m_%d-%H_%M_%S")"