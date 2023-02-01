#!/usr/bin/bash


git pull
systemctl restart cd-assignment.service
echo 'succesfully updated!'
