#!bin/bash

echo "setting up nginx & uwsgi config ..."
sudo bash -c "cat /home/sites/api.propiet.com/propietapi/setup/nginx.conf >> /etc/nginx/sites-available/default"
sudo cp /home/sites/api.propiet.com/propietapi/setup/propietapi.ini /etc/uwsgi/apps-available/propietapi.ini
sudo ln -s /etc/uwsgi/apps-available/propietapi.ini /etc/uwsgi/apps-enabled/propietapi.ini

echo "restarting services ..."
sudo service nginx restart
sudo service uwsgi restart

echo "applying database config ..."
cd /home/sites/api.propiet.com/propietapi && python manage.py syncdb
cd /home/sites/api.propiet.com/propietapi && python manage.py migrate

sudo service uwsgi restart

echo "done!"
