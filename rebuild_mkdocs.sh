#!/bin/bash

cp ./keys/jenkins/id_rsa* ./dockerfiles/jenkins/.ssh
cp ./keys/mkdocs/id_rsa* ./dockerfiles/mkdocs/.ssh

docker compose up --detach --build mkdocs

rm ./dockerfiles/jenkins/.ssh/id_rsa*
rm ./dockerfiles/mkdocs/.ssh/id_rsa*
