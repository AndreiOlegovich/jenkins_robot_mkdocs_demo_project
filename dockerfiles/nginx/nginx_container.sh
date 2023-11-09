#!/bin/bash

# service ssh start
/usr/sbin/sshd -D &
# service nginx start
# /etc/init.d/nginx start
/usr/sbin/nginx &

wait -n

exit $?