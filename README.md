[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-376)
![PyPI](https://img.shields.io/pypi/v/django?label=django)
![PyPI](https://img.shields.io/pypi/v/djangorestframework?label=Django%20REST%20framework)
# Profiles API REST with django_rest_framework

Is an API Rest example with jwt authentication and custom permissions.

# INSTALL PROJECT

## PREPARE VIRTUALENV
* virtualenv -p python3 profilesvenv
* source profilesvenv/bin/activate

## CLONE PROJECT
git clone git@github.com:carpancan/django_rest_framework.git

## INSTALL ALL DEPENDENCIES
pip install -r django_rest_framework/requirements.txt

## CREATE SUPERUSER TO START USE API
* cd django_rest_framework
* python manage.py migrate
* python manage.py createsuperuser

# RUN PROJECT
python manage.py runserver

# COMMANDS
python manage.py 

Available subcommands:

### [account]
    * account_unsetmultipleprimaryemails

### [auth]
    * changepassword
    * createsuperuser

### [authtoken]
    * drf_create_token

### [contenttypes]
    * remove_stale_contenttypes

### [django]
    * check
    * compilemessages
    * createcachetable
    * dbshell
    * diffsettings
    * dumpdata
    * flush
    * inspectdb
    * loaddata
    * makemessages
    * makemigrations
    * migrate
    * sendtestemail
    * shell
    * showmigrations
    * sqlflush
    * sqlmigrate
    * sqlsequencereset
    * squashmigrations
    * startapp
    * startproject
    * test
    * testserver

### [rest_framework]
    * generateschema

### [sessions]
    * clearsessions

### [staticfiles]
    * collectstatic
    * findstatic
    * runserver

# RUN TESTS
python manage.py test
