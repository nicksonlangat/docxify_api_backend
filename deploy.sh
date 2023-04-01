#!/bin/bash
echo "Starting the deployment process"

#pull from the branch
git pull origin main

#activate the django env
source env/bin/activate

#install deps
pip install -r requirements.txt

#apply any migrations
python manage.py migrate

#exit the env
deactivate 

#restart daemon
sudo systemctl daemon-reload

#restart gunicorn 
sudo systemctl restart doc

#restart nginx
sudo systemctl restart nginx

echo "That looks good, code deployed with success :)"