#!/bin/bash

apt install -y dos2unix

cp ./keys/jenkins/*rsa* ./dockerfiles/jenkins/.ssh
cp ./keys/mkdocs/id_rsa* ./dockerfiles/mkdocs/.ssh

dos2unix dockerfiles/mkdocs/entrypoint.sh
dos2unix dockerfiles/robot/entrypoint.sh
docker compose build
docker compose up -d

rm ./dockerfiles/jenkins/.ssh/*rsa*
rm ./dockerfiles/mkdocs/.ssh/id_rsa*
