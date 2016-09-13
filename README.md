## CSV-Flask Install Guide


#### This repository has 3 parts:

##### sitebuilder.py - Dynamic page generator using Flask (minimal Web framework for Python)

##### videos.html - Front page template in Jinja2

##### videos.csv — Comma-separated metadata for each item on site, including video links. YouTube videos with 'TRUE' in 'Display Video' field will embed automatically. Rearranging and/or adding columns won't disrupt the page generator, but be sure to leave the column headers intact. Not all fields are currently displayed.
     ['Creator', 'Piece Title', 'Year', 'Date', 'Date Published', 'Event Name', 'Format/Genre', 'Venue', 'City', 'State/Province', 'Country', 'Notes', 'Tags', 'Display Video', 'Video URL', 'Text/Event URL', 'Language', 'License', 'Date Accessed']



## Installing


#### SSH to server and make sure you have the needed dependencies.

     pip install -U Flask jinja2 python-tablefu

     apt-get install git

#### Now clone the code from GitHub.

     cd /home

     git clone https://github.com/stevemclaugh/csv-flask.git

     cd csv-flask

#### Stop the Apache server to free up port 80. In Ubuntu, that looks like the following:

     /etc/init.d/apache2 stop

#### Create default shortcut Flask expects.

     export FLASK_APP=/home/csv-flask/sitebuilder.py

#### Now start Flask to display your site to the public. Use a different port if you prefer.

     flask run --host=0.0.0.0 --port=80

#### Uncomment and use this instead to keep the script running after you end the current ssh session.

     #nohup flask run --host=0.0.0.0 --port=80

#### Uncomment and run this command to start the Apache server again (or just reboot server and it will launch by default).

     #/etc/init.d/apache2 start


####

#### So far, pages are generated dynamically by creator field and by tags (which are comma-separated in CSV metadata).

     http://138.68.61.170/creator/Holly_Melgard/

     http://138.68.61.170/tag/collaboration/



####

#### CC0 1.0 Universal (CC0 1.0)

#### https://creativecommons.org/publicdomain/zero/1.0/
