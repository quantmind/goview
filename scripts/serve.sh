#!/usr/bin/env bash

gunicorn --workers=1 --worker-class=meinheld.gmeinheld.MeinheldWorker -b :7000 goview:app
