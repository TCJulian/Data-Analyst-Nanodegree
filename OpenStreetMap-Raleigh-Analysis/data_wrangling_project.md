# OpenStreet Map Data Wrangling Project

## Overview

Raleigh-Durham, NC OSM file download: https://mapzen.com/data/metro-extracts/metro/raleigh_north-carolina/

Audit and conversion from XML to CSV took approximately 30 minutes.

## Problems while Auditing/Converting OSM file

* Depreciated second level "key" tags in node and way tags (_"name_1", "Street_1", and "zipcode"_)
* Various formats of phone numbers (_"+1-(919)-680-6333", "919 908 1023"_)
* Zip+4 postal code format (_"27603-1407"_)
* Inconsistent street name abbreviations (_"Crawford Ct", "Chapel Hill Rd"_)
* tiger and NHD data sources in second level "key" tags
* Carriage return values in SQL entries upon XML to csv converions

### Standardizing Phone Numbers
Phone numbers in the dataset came in various formats. Some had the +1 country code, while other used parenthesis around the area code. Some uses dashes to separate the different sections of the number while other used spaces.

In order to standardize these numbers, I used a regular expressions to strip any non-digit characters out of the phone number. The format I am looking for is an optional country code, followed by ten digits. 

For example, the number `+1-(919)-680-6333` would become `19196806333`.

Here is a snippet of the code that audits the phone number into the above format:
~~~~PYTHON
correct_re = re.compile(r'1?\d{10}$')

if not correct_re.search(num):
    num = re.sub(r'\D', '', num)
    if not correct_re.search(num):
        num = "***Unknown format. No changes made.***"
        return num
return num
~~~~


### Trimming Postal Codes

### Street Name Abbreviations

## Overview of database 

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


### Top Ten Amenities for nodes
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

### Major Cities in nodes
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

### Major Counties in ways
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

## Ideas for Additional Improvement

## Conclusion
