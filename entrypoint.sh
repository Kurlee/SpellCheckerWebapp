#!/bin/bash

mkdir -p /code/logs
touch /code/logs/gunicorn.log
touch /code/logs/gunicorn-access.log
tail -n 0 -f /code/logs/gunicorn*.log


exec gunicorn "SpellCheckApp:create_app()" \
    --name spelling-docker \
    --bind 0.0.0.0:8080 \
    --workers 5 \
    --log-level=info \
    --log-file=/code/logs/gunicorn.log \
    --access-logfile=/code/logs/gunicorn-access.log \
"$@"