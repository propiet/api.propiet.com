# Propiet API README

## Development

### System Dependencies

* virtualenv
* python2.7

## Setup development environment

* Clone the repo: ``git clone git@git.devartis.com:propiet-api.git``
* Go to propietapi dir: ``cd propiet-api/propietapi``
* Create virtualenv: ``mkvirtualenv propiet-api``
* Install dependencies: ``pip install -r requirements/dev.txt``
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

## Nginx with headers-more module

* Download nginx source code: ``wget 'http://nginx.org/download/nginx-1.4.6.tar.gz'``
* Download headers-more source code: ``wget https://github.com/openresty/headers-more-nginx-module/archive/v0.25.tar.gz -O headers-more-nginx-module-v0.25.tar.gz``
* Uncompress source code tarballs: ``tar -xzvf nginx-1.4.6.tar.gz && tar -xzvf headers-more-nginx-module-v0.25.tar.gz``
* Compile nginx with headers-more module. nginx will be installed on ``/opt/nginx/``:
    * ``cd /path/to/nginx-1.4.6``
    * ``./configure --prefix=/opt/nginx --add-module=/path/to/headers-more-nginx-module-0.25``
    * ``make && sudo make install``
* Configure upstart script to run nginx as a service:


    echo "# nginx
description 'nginx http daemon'
author 'Philipp Klose'

start on (filesystem and net-device-up IFACE=lo)
stop on runlevel [!2345]

env DAEMON=/opt/nginx/sbin/nginx
env PID=/opt/nginx/logs/nginx.pid

expect fork
respawn
respawn limit 10 5
#oom never

pre-start script
$DAEMON -t
if [ $? -ne 0 ]
then exit $?
fi
end script

exec $DAEMON" | sudo tee -a /etc/init/nginx_with_headers_more.conf

* Start nginx with: ``sudo service nginx_with_headers_more start``
* Create a directory to hold nginx config files and set its permissions: ``sudo mkdir /opt/nginx/sites-available && sudo chown nobody:root /opt/nginx/sites-available``
* Add ``import`` statement inside ``http`` block on ``/opt/nginx/nginx.conf`` file: ``import /opt/nginx/sites-available/*;``
* Create a symlink to the PHP app nginx config file: ``sudo ln -s /home/poli/work/php/propiet-com/dev.propiet.com.conf /opt/nginx/sites-available/dev.propiet.com.conf``
* Create a symlink to the Python app nginx config file: ``sudo ln -s /home/poli/work/python/propiet-api/propietapi/dev-api.propiet.com.conf /opt/nginx/sites-available/dev-api.propiet.com.conf``
* Restart nginx: ``sudo service nginx_with_headers_more restart``

## Production / Staging


### Get the source code

* Clone this repo inside /path/to/propiet/api/dir: ``mkdir -p /path/to/propiet/api/dir && cd /path/to/propiet/api/dir && git clone git@git.devartis.com:propiet-api .``

### Install pyenv

* ``curl -L https://raw.githubusercontent.com/yyuu/pyenv-installer/master/bin/pyenv-installer | bash``
* ``pyenv update``
* ``PYTHON_CONFIGURE_OPTS="--enable-unicode=ucs4" pyenv install 2.7.6``
* ``git clone https://github.com/yyuu/pyenv-virtualenvwrapper.git ~/.pyenv/plugins/pyenv-virtualenvwrapper``
* ``echo "export WORKON_HOME=~/.env" >> ~/.bashrc``
* Close SSH session / Login again
* ``cd /path/to/propiet/api/dir``
* ``pyenv local 2.7.6``
* ``pyenv virtualenvwrapper``
* ``mkvirtualenv propiet-api-prod``
* Config hooks: ``cdvirtualenv && echo "export OLD_DJANGO_SETTINGS_MODULE=\$DJANGO_SETTINGS_MODULE
export DJANGO_SETTINGS_MODULE=settings.prod" >> bin/postactivate && echo "export DJANGO_SETTINGS_MODULE=\$OLD_DJANGO_SETTINGS_MODULE" >> bin/postdeactivate && cd - && deactivate && workon propiet-api-prod``
* ``pip install -r requirements/prod.txt``

### uwsgi and nginx configuration

* Map uwsgi config file: ``sudo ln -s /path/to/propiet/api/dir/propietapi/setup/prod/api.propiet.com.ini /etc/uwsgi/apps-available/ && sudo ln -s /etc/uwsgi/apps-available/api.propiet.com.ini /etc/uwsgi/apps-enabled/``
* Map nginx config file: ``sudo ln -s /path/to/propiet/api/dir/propietapi/setup/prod/api.propiet.com.conf /etc/nginx/sites-available/ && sudo ln -s /etc/nginx/sites-available/api.propiet.com.conf /etc/nginx/sites-enabled/``
* Restart both services: ``sudo service uwsgi restart && sudo serice nginx restart``
* Access to the admin http://api.propiet.com/admin

*System dependencies*

* make
* build-essential
* zlib1g-dev
* libbz2-dev
* libreadline-dev
* libsqlite3-dev
* wget
* curl
* llvm
* libssl-dev
* uwsgi
* uwsgi-plugin-python
* nginx
* HttpHeadersMoreModule
* erlang
* erlang-nox
* libtiff4-dev
* libmysqlclient-dev
* libjpeg8-dev
* zlib1g-dev
* libfreetype6-dev
* liblcms2-dev
* libwebp-dev
* tcl8.5-dev
* tk8.5-dev
* python-tk
* git

### Install RabbitMQ

* ``sudo apt-get install erlang erlang-nox``
* ``wget http://www.rabbitmq.com/releases/rabbitmq-server/v3.3.4/rabbitmq-server_3.3.4-1_all.deb``
* ``sudo dpkg -i rabbitmq-server_3.3.4-1_all.deb``
* ``sudo apt-get -f install # Esto es para finalizar la instalacion``

#### User config

* sudo rabbitmqctl add_user propiet propiet
* sudo rabbitmqctl add_vhost propiet
* sudo rabbitmqctl set_permissions -p propiet propiet ".*" ".*" ".*"
