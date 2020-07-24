#!/bin/bash

touch /var/log/flask.log
chmod 666 /var/log/flask.log

/usr/sbin/apache2ctl -D FOREGROUND