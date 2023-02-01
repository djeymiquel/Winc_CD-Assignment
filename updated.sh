#!/usr/bin/bash

git pull
sudo systemctl restart nginx
echo 'succesfully updated!'
