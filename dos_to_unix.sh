#!/bin/bash

apt install -y dos2unix

dos2unix dockerfiles/mkdocs/entrypoint.sh
dos2unix dockerfiles/robot/entrypoint.sh

