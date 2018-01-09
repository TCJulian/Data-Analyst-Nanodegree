# OpenStreet Map Data Wrangling Project

## Overview

Raleigh, North Carolina OSM file download: https://mapzen.com/data/metro-extracts/metro/raleigh_north-carolina/

## Problems while Auditing OSM file

* name_1 key is a depreciated key.
* tiger and NHD data sources

## Overview of data

### Size of files
~~~~
raleigh_north-carolina.osm ......... 465.0 MB
OSM_db.db .......................... 250.0 MB
nodes.csv .......................... 183.0 MB
ways_nodes.csv .....................  60.7 MB
ways_tags.csv ......................  29.6 MB
ways.csv ...........................  13.4 MB
nodes_tags.csv .....................   2.1 MB
~~~~

## Resources

* [TagInfo](https://taginfo.openstreetmap.org/keys). Identifies the usage and meaning of different keys in OSM files. 
* Python Documentation
  * [regex](https://docs.python.org/3/library/re.html?s)
  * [The ElementTree XML API](https://docs.python.org/3/library/xml.etree.elementtree.html?)
* SQL Style Guides
  * [sqlstyle](http://www.sqlstyle.guide/)
* SQL Tutorials:
  * [UNION clause](https://www.tutorialspoint.com/sqlite/sqlite_unions_clause.htm)
* StackOverflow
  * [Printing Dictionaries to Files](https://stackoverflow.com/questions/36965507/writing-a-dictionary-to-a-text-file-in-python)
  * [Removing carriage return values from sqlite](https://pvanb.wordpress.com/2011/01/13/finding-and-removing-carriage-returns-in-your-sqlite-table/)
  * [Using Variables in re](https://stackoverflow.com/questions/6930982/how-to-use-a-variable-inside-a-regular-expression)
