NS = quantmind
REPO = goview

# set version if absent
VERSION ?= latest
DOCKER_IMAGE ?= ${NS}/${REPO}:${VERSION}
PYTHON ?= python
PIP ?= pip

.PHONY: help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

image:	## Build the docker image
	docker build -t $(NS)/$(REPO):$(VERSION) .

test:	## Run unit tests
	$(PYTHON) -m flake8
	$(PYTHON) setup.py test -q --io uv

shell:	## Enter bash shell in container
	docker run --rm -it $(NS)/$(REPO):$(VERSION) /bin/bash

push:	## Push image to dockerhub
	docker push $(NS)/$(REPO):$(VERSION)

serve:	## Run prod server
	docker run --rm $(NS)/$(REPO):$(VERSION)
