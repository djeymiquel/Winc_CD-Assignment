#!/usr/bin/bash
git commit -m "updated"
git pull
sudo systemctl restart nginx
echo "Succesfully updated"
