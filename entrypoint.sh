#!/bin/bash


if [ ! -e "$VIRTUAL_ENV/bin" ]; then
    echo "Creating virtualenv at \"$VIRTUAL_ENV\""
    python -m venv "$VIRTUAL_ENV"
fi

if [ "$INITIAL" = "1" ]; then
    if [ ! -e "requirements/dev.txt" ]; then
        pip install pip-tools
        pip-compile requirements/dev.in
    fi

    pip install -r requirements/dev.txt

   # if [ ! -e "requirements/test.txt" ]; then
    #    pip-compile requirements/test.in
    #fi


    # Wait for the db server to be ready, then run the migrate command
    while ! (echo > /dev/tcp/db/5432) >/dev/null 2>&1; do echo -n '.'; sleep 1; done;
    echo "Running migrations..."
    exec /venv/bin/python ./manage.py migrate
fi

exec "${@}"
