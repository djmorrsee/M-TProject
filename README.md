Methods and Tools Project
=========================

## Daniel Morrissey and Andrey Shprengel

### About

We are aiming to develop a system of 'modules,' which are microcontrollers equipped
with temperature and light sensors. These modules will take their readings and send them
to a centralized server. The server, along with simply storing the data, will
be in charge of presenting a web site for monitoring the module data.


### The Server - Website

The current plan is to use a python Flask server to handle the website

Typical HTML5 suite for website (HTML, CSS, JQuery, Bootstrap CSS framework)

For graphing our data on the web page, we should select one of these jquery based libraries:

>- http://www.jqplot.com/
>- http://www.flotcharts.org/
>- http://www.jchartfx.com/

### The Server - Storage

Flask/Python couples well with sqlite3 or sqlalchemy

Is a database the best way to store this simple data? Would CSV's be sufficient?
A full on SQL db seems overkill for continuous data.

### The Modules

The pcDuinos will be programmed in C/Arduino-C/Python

The act of sending the data from the module to the server will be done in python.
