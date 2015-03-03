# for more on gunicorn logging, see http://docs.gunicorn.org/en/latest/settings.html#logging
web: NEW_RELIC_CONFIG_FILE=newrelic.ini newrelic-admin run-program gunicorn --timeout 300 api.wsgi --log-file -
