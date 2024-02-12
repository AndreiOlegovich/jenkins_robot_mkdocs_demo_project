#!/bin/bash

# touch "ENTRYPOINT.txt" 
# echo $(whoami) > ENTRYPOINT.txt
# python -m mkdocs build
cp -r site /home/jenkins/mkdocs/documentation
service ssh start
tail -f /dev/null