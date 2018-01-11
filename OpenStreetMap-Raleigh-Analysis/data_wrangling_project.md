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

### Number of Unique Users
~~~~SQL
SELECT COUNT(*)
    FROM (  SELECT user
              FROM nodes
        
             UNION

            SELECT user
              FROM ways) AS total_users;
~~~~

971

### Number of nodes
~~~~SQL
  SELECT COUNT(*) 
    FROM nodes;
~~~~

2347549


### Number of ways
~~~~SQL
  SELECT COUNT(*) 
    FROM ways;
~~~~

241260


#### Top Ten Amenities for nodes
~~~~SQL
   SELECT value, COUNT(*) 
     FROM nodes_tags 
    WHERE key = 'amenity' 
 GROUP BY value 
 ORDER BY COUNT(*) DESC 
    LIMIT 10;
~~~~
~~~~SQL
bicycle_parking  573
restaurant       451
place_of_worshi  371
fast_food        183
bench            131
waste_basket     124
cafe             96
atm              78
school           76
parking          70
~~~~

### Top Five Contributors
~~~~SQL
  SELECT user, COUNT(*)
    FROM (  SELECT user
              FROM nodes

             UNION ALL

            SELECT user
              FROM ways) AS total_users 
GROUP BY user 
ORDER BY COUNT(*) DESC
   LIMIT 5;
~~~~
~~~~SQL
jumbanho         1556845
JMDeMai          219539
bdiscoe          129730
woodpeck_fixbot  113815
bigal945         103684
~~~~

#### Major Cities in nodes
~~~~SQL
  SELECT value, COUNT(*) 
    FROM nodes_tags 
   WHERE key = 'city' 
GROUP BY value 
ORDER BY COUNT(*) DESC
   LIMIT 5;
~~~~
~~~~SQL
Cary             294
Durham           289
Raleigh          238
Carrboro         143
Chapel Hill      83
~~~~

#### Major Counties in ways
~~~~SQL
  SELECT value, COUNT(*) 
    FROM ways_tags 
   WHERE key="county" 
GROUP BY value 
ORDER BY COUNT(*) DESC 
   LIMIT 5;
~~~~
~~~~SQL
Wake, NC         9421
Durham, NC       5212
Orange, NC       2188
Chatham, NC      442
Granville, NC;   25
~~~~

### Max/Min Longitudes and Latitudes
~~~~SQL
SELECT MAX(lon) AS max_lon, 
       MIN(lon) AS min_lon,
       MAX(lat) AS max_lat,
       MIN(lat) AS min_lat 
FROM nodes;
~~~~
~~~~
max_lon          min_lon      max_lat     min_lat
---------------  -----------  ----------  ----------
-78.577          -79.1159995  36.0509986  35.759
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
