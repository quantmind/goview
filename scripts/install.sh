#!/usr/bin/env bash

pip install -U pip wheel
pip install -U setuptools
pip install -U -r scripts/requirements/hard.txt
pip install -U -r scripts/requirements/prod.txt
pip install -U -r scripts/requirements/dev.txt
