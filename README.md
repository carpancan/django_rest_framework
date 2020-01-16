# Profiles API REST with django_rest_framework

Is an API Rest example with jwt authentication and custom permissions.

#INSTALL PROJECT

##prepare virtualenv
virtualenv profilesvenv
source profilesenv/bin/activate

##clone project
git clone git@github.com:carpancan/django_rest_framework.git

##install all dependencies
pip install -r django_rest_framework/requirements.txt

#RUN PROJECT
cd django_rest_framework
python manage.py runserver

#COMMANDS
Type 'manage.py help <subcommand>' for help on a specific subcommand.

Available subcommands:

[account]
    account_unsetmultipleprimaryemails

[auth]
    changepassword
    createsuperuser

[authtoken]
    drf_create_token

[contenttypes]
    remove_stale_contenttypes

[django]
    check
    compilemessages
    createcachetable
    dbshell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[rest_framework]
    generateschema

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver


