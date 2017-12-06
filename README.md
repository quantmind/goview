# goview

A simple web-app with python 3, flask and d3js


## Dev setup

This web app requires python 3.5 or above, therefore you need a valid python 3 installation.
Check the version by
```
python3 --version
```
make sure you have [virtualenv](https://pypi.python.org/pypi/virtualenv)
installed so that you can setup the virtual environment for development.
From inside the toplevel directory execute
```
virtualenv venv
source venv/bin/activate
./scripts/install.sh
```
Almost there, but before you can start you need to setup the database by running the migration script
```
./scripts/dev.sh db upgrade
```
Run the dev server with
```
./scripts/dev.sh run --reload
```
To run unittests simply invoke
```
flake8 && nosetests
```

## Docker

A [Dockerfile](./Dockerfile) is supplied and the image can be build by
```
make image
```
Other commands can be run with make, to see the list type
```
make help
```
