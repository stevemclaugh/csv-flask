## CSV-Flask Readme


#### This repository has 3 components:

* sitebuilder.py - Dynamic page generator using Flask (minimal Web framework for Python)

* videos.html - HTML page template in Jinja2

* videos.csv - Comma-separated metadata for each item on site, including video links. Rearranging and/or adding columns won't disrupt the page generator, but be sure to leave the column headers intact. Not all metadata fields are currently displayed. YouTube videos with 'TRUE' in 'Display Video' field will embed automatically.

     ['Creator', 'Piece Title', 'Year', 'Date', 'Date Published', 'Event Name', 'Format/Genre', 'Venue', 'City', 'State/Province', 'Country', 'Notes', 'Tags', 'Display Video', 'Video URL', 'Text/Event URL', 'Language', 'License', 'Date Accessed']


## Installation


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

#### Or use this command to keep the site running after you close your shell session.

     nohup flask run --host=0.0.0.0 --port=80

#### That's it! If you made it through without errors, the site should be up and running.

#### Pages are generated dynamically by creator field and by individual tags (which are separated by commas in the CSV metadata).

     *your_domain*/creator/Holly_Melgard/

     *your_domain*/tag/collaboration/
     

#### If you want to restart the Apache server, run this command (or just reboot and it will launch by default).

     /etc/init.d/apache2 start



#### 

#### To learn more, see the following tutorials (from which I cribbed some of this code):

http://blog.apps.chicagotribune.com/2010/12/07/from-spreadsheet-to-html-in-15-minutes-with-python-tablefu-jinja-and-flask/

https://nicolas.perriault.net/code/2012/dead-easy-yet-powerful-static-website-generator-with-flask/


#### CC0 1.0 Universal (CC0 1.0)

https://creativecommons.org/publicdomain/zero/1.0/

