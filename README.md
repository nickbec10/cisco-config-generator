CSV Based Config Generator
==============

This repository contains a simple Cisco configuration generator using python and jinja2. This one takes in a CSV parameter file but could esily be modified to use JSON.


Installation
------------

Just clone this repository, then install the necessary python packages. Remember to use take advantage of the virtual environment if you are using one.

To run you need to install Jinja2 to your python environment, using the following command:
```bash
$ pip install jinja2
```


Usage
-----

The script takes 2 command line arguments; a template file to write from and a parameter file to read from.
It will output config files into a folder called output.

```bash
$ python csv_based_config_generator.py -t template.j2 -c parameters.csv
```
