#!/bin/bash

cp /start-apis/server.py /apis/apis-webpage-base/apis/settings/server.py
cp /start-apis/wsgi.py /apis/apis-webpage-base/apis/wsgi.py
cd /apis/apis-webpage-base
git pull
if [ -z "$APIS_BASE_BRANCH" ]; then
	if [ `git branch --list $APIS_BASE_BRANCH` ]; then
		git checkout "$APIS_BASE_BRANCH"
		echo "checking out local branch"
	else
		git checkout -b "$APIS_BASE_BRANCH" origin/"$APIS_BASE_BRANCH"
	fi
fi
cd apis_core
git pull
cd ..
python manage.py collectstatic --noinput --settings=apis.settings.server
gunicorn apis.wsgi:application --log-level DEBUG --bind 0.0.0.0:8000
