Methods and Tools Project Summer 2014
=========================

###Daniel Morrissey and Andrey Shprengel

## Project Repositories

### The Server Repo

>- https://github.com/djmorrsee/M-TProject

This is the repository for the flask server.

### The Duino Repo

>- https://github.com/djmorrsee/python-pcduino

This is the Arduino deployment repo. This repo was originally forked from
https://github.com/pcduino/python-pcduino

### Documentation

>- https://github.com/djmorrsee/mtdocs

The documentation for the repositories can be found at the above url. Built
using Sphinx-Doc. We felt providing the documentation would be easier than giving
build instructions for both repositories.

## Running Requirements

### Server:

Run:

>- python server

API:

	/all/ 				- GET - Retrieve all data
	/module/ 	 		- GET - Retrieve data for module
	/module/<id>/ 		- GET/POST/DELETE - List, register or remove a module
	/module/post_reading/ - POST - Module data posting route
	/drop/				- DELETE - Drop old data from table
	/reset/	 	 	 - DELETE - Reset the entire table

Required Python Libraries:

>- flask
>- sqlalchemy
>- flask-sqlalchemy
>- requests

### Dunio:

Run:

>- python register_module
>- python unregister_module
>- python take_reading
>- python reset_table


Required Python Libraries:

>- requests

Other Requirements:

>- Needs to be run on a duino.
>- Needs a constants.py in bin/util. Ignored for security reasons
