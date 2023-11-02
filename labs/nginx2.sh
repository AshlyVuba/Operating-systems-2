#!/bin/bash

dir= "labs"
link= "html"
page= "index.html"

echo 'NGINX CONFIG SCRIP##'
echo 'SCRIPT INTIALISING...'
sleep 1

if (systemct1 is-active nginx)
then
     echo "service running..."
     sleep 1
     echo "creating directory labs"
     sleep 1
     mkdir /var/www/html/$dir
     sleep 1
     chown phil /var/www/html/labs
     sleep 1
     echo "creating symbolic link.."
     ln -s /var/www/html/$dir $link
     ls -l
     echo "creating test page $page"
     sleep 1
     cd html
     touch $page
     sleep 1
echo "<html>" > $page
    echo "<body>" >> $page
    echo "<h1> Welcome to My Page!</h1>" >> $page
    echo "</body>" >> $page
    echo "</html>" >> $page


else
     echo "NGINX SERVICE NOT RUNNING!"
     apt-get update
     apt-get -y install nginx
     sleep 1
     exit 1
fi
