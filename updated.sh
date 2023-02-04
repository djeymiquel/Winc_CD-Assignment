#!/usr/bin/bash

git pull
sudo systemctl restart nginx
echo "Successfully updated"
