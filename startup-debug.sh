#!/bin/bash

touch /var/log/flask.log
chmod 666 /var/log/flask.log

python /var/www/apache-flask/run.py