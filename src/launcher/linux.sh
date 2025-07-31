#!/bin/bash
cd "$(dirname $(realpath "$0"))"
./bin/ld-linux-x86-64.so.2 --library-path ./bin ./bin/lyra "$@"