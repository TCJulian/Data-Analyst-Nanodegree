# OpenStreet Map Data Wrangling Project

## Overview

Raleigh-Durham, NC OSM file download: https://mapzen.com/data/metro-extracts/metro/raleigh_north-carolina/

Audit and conversion from XML to CSV took approximately 30 minutes.

## Problems while Auditing/Converting OSM file

* Depreciated second level `"k"` tags in `"nodes_tags"` and `"ways_tags"` (_"name_1", "Street_1", and "zipcode"_)
* Various formats of phone numbers (_"+1-(919)-680-6333", "919 908 1023"_)
* ZIP+4 postal code format (_"27603-1407"_)
* Inconsistent street name abbreviations (_"Crawford Ct", "Chapel Hill Rd"_)
* tiger and NHD data sources in second level `"k"` tags
* Carriage return values in database entries upon XML to CSV converion

### Standardizing Phone Numbers
Phone numbers in the dataset came in various formats. Some had the +1 country code while others included parentheses around the 3-digit area code. The format for spacing also varied between numbers, with some using dashes to separate the different sections while others used spaces.

In order to standardize these numbers, I used regular expressions to strip any non-digit characters out of the phone number. The standard format for this dataset would have an optional country code followed by ten digits. 

For example, the number `+1-(919)-680-6333` would become `19196806333`.

Here is a snippet of the code that audits the phone number into the above format:
~~~~PYTHON
correct_re = re.compile(r'1?\d{10}$')

def check_phone(num):
    """Returns phone number with all non-digit characters removed."""
    if not correct_re.search(num):
        num = re.sub(r'\D', '', num)
        if not correct_re.search(num):
            num = "***Unknown format. No changes made.***"
            return num
    return num
~~~~

With all of the numbers in the same format, querying and sorting phone numbers from the database became much easier.

### Trimming Postal Codes

The most popular format for postal codes in this data set was the ZIP+4 format (_"27603-1407"_). While this type of postal code provides an extra level of detail, it also makes querying and aggregates postal codes together much more difficult.

To standardize the postal codes, all ZIP+4 formats were trimmed of their last four digits and the trailing `"-"`.
Other cleaning was also done, including removing any non-digit characters.

~~~~SQL
  SELECT value, COUNT(*) 
    FROM nodes_tags 
   WHERE key = "postcode" 
GROUP BY value 
ORDER BY COUNT(*) DESC 
   LIMIT 10;
~~~~
~~~~
27701|164
27513|149
27510|143
27511|94
27560|66
27519|52
27601|47
27705|44
27707|40
27514|33
~~~~

### Street Name Abbreviations

Using a combination of expected values, mappings, and regular expressions, I was able to make a system that corrects the most popular abbrevations in street names. 

Implemented in all of the audit scripts code that writes the changes to a text file, so that the changes can be reviewed after the XML to CVS conversion and audit is complete. The left side is the old value, while the right side is the corrected value. Exceptions not corrected by the audit remained unchanged in the final CSV file, while a special reply is inserted in the text file to bring attention to the exception. This exception allows the user to update the mapping in the script accordingly.

A sample of this text file is provided below:
~~~~
[["Falls of Neuse Rd", "Falls of Neuse Road"]]
[["Waterford Lake Dr", "Waterford Lake Drive"]]
[["Waterford Lake Dr", "Waterford Lake Drive"]]
[["Buck Jones Rd", "Buck Jones Road"]]
[["Meadowmont Village CIrcle", "***Unknown Mapping. No changes made.***"]]
[["Creedmoor Rd", "Creedmoor Road"]]
[["Main at North Hills St", "Main at North Hills Street"]]
[["Durham-Chapel Hill Blvd.", "Durham-Chapel Hill Boulevard"]]
~~~~
### Removing carriage return values from database

After creating the database tables in SQLite, I attempted to import the CSV files. However, upon doing do, I found that many of the values, especially those 

To resolve this issue, I wrote a short Python script that programmatically removes the carriage return values from the database values.

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
