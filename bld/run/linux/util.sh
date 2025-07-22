#!/bin/bash

isLinux() {
    if [[ "$(uname)" != "Linux" ]]; then
        echo -e "This script must run on Linux!"
        exit 1
    fi
}

runDocker() {
    isLinux

    sudo docker build -f "Dockerfile.linux" -t "lyra-env:latest" .
    sudo docker rm "lyra-env"
    sudo docker run --name "lyra-env" "lyra-env:latest" $1
}

copyDocker() {
    sudo docker cp "lyra-env:/Lyra/$1" "./$2"
}