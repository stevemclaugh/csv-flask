#!/usr/bin/env python
# -*- coding: utf-8 -*-
 
import jinja2
import table_fu
from flask import Flask
import csv

DATA_FILE = 'data/videos.csv'
TEMPLATE_DIR = 'templates'
TEMPLATE_FILE = 'videos.html'

app = Flask(__name__)
 
@app.route("/")
def main():
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    temp_table=[]
    with open(DATA_FILE, 'U') as fi:
		mydata = csv.reader(fi)
		for row in mydata:
			temp_table.append([item.decode('utf-8') for item in row])
    table = table_fu.TableFu(temp_table)
    html = env.get_template(TEMPLATE_FILE).render(table=table)
    return html

@app.route('/creator/<string:creator>/')
def creator(creator):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    temp_table=[]
    with open(DATA_FILE, 'U') as fi:
		mydata = csv.reader(fi)
		for row in mydata:
			temp_table.append([item.decode('utf-8') for item in row])
    table = table_fu.TableFu(temp_table)
    t2 = table.filter(Creator=creator.replace("_"," "))
    html = env.get_template(TEMPLATE_FILE).render(table=t2)
    return html

@app.route('/tag/<string:tag>/')
def tag(tag):
    env = jinja2.Environment(loader=jinja2.FileSystemLoader(TEMPLATE_DIR))
    temp_table=[]
    with open(DATA_FILE, 'U') as fi:
		mydata = csv.reader(fi)
		for row in mydata:
			temp_table.append([item.decode('utf-8') for item in row])
    table = table_fu.TableFu(temp_table)
    flat_table=[]
    flat_table.append(table._get_columns())
    for row in table:
        if str(tag).lower() in [item.lower().strip() for item in str(row['Tags']).split(',')]:
            flat_table.append(list(row))
    t2=table_fu.TableFu(flat_table)
    html = env.get_template(TEMPLATE_FILE).render(table=t2)
    return html

@app.route('/<path:path>/')
def page(path):
	return "Nothing here at the moment."

if __name__ == "__main__":
    app.run(host='0.0.0.0',port=80)
