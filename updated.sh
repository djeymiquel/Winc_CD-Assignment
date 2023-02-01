#!/usr/bin/bash

git pull
sudo systemctl restart cd-assignment.service
echo 'succesfully updated!'
