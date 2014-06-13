# Propiet API README

## Development

### System Dependencies

* virtualenv
* python2.7

## Setup development environment

* Clone the repo: ``git clone git@git.devartis.com:propiet-api.git``
* Go to propietapi dir: ``cd propiet-api/propietapi``
* Create virtualenv: ``mkvirtualenv propiet-api``
* Install dependencies: ``pip intall -r requirements/dev.txt``
* Edit your virtualenv's postactivate hook:
    * ``cdvirtualenv``
     * ``echo "export DJANGO_SETTINGS_MODULE='settings.dev_jrio'
export DJANGO_DEV=1" >> bin/postactivate``
     * ``cd -``
     * ``deactivate``
     * ``workon propiet-api``
* Syncdb without creating superuser: ``./manage.py syncdb --noinput --migrate``
* Create the superuser: ``./manage.py createsuperuser``
* Collect static files: ``./manage.py collectstatic``
* Run the web server: ``./manage.py runserver 0.0.0.0:8000``
* Browse to ``http://localhost:8000/admin``


## Production / Staging

* Clone this repo inside the /home/sites folder.
* Add to your hosts file on local machine (/etc/hosts) 192.168.56.101 api.propiet.com
* Run the file ('''run.sh ''') inside setup folder.

* Access to the admin http://api.propiet.com/admin

*System dependencies*

* uwsgi
* uwsgi-plugin-python
* nginx
* HttpHeadersMoreModule
