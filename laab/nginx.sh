#!/bin/bash
sudo apt-get update
sudo apt-get -y install nginx
systemctl is active nginx
sudo mkdir /var/www/html/labs
sudo chowm 221762353 /var/www/html/labs
ln -s /var/www/html/labs
