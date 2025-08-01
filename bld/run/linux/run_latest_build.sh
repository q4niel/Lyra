#!/bin/bash
cd "$(dirname $(dirname $(dirname $(dirname $(realpath "$0")))))"

if ! [ -d bld/out ]; then
    echo "No builds available!"
    exit 1
fi

latestBuild=$(ls -1d bld/out/????_??_??-??_??_?? | sort | tail -n 1)
sh "$latestBuild/Lyra/Lyra"