# SQL Queries 

This file holds all of the different queries done on the database. All queries may not be included in the final report.
## General

#### Total nodes and ways
~~~~SQL
SELECT COUNT(*) 
  FROM (SELECT id 
          FROM nodes 
          
         UNION ALL 
          
        SELECT id 
          FROM ways) AS total_rows;
~~~~

#### Total Unique Users
~~~~SQL
  SELECT COUNT(*)
    FROM (  SELECT user
              FROM nodes
        
             UNION

            SELECT user
              FROM ways) AS total_users;
~~~~

#### Top Five Contributors
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

### Max/Min Longitudes and Latitudes
~~~~SQL
SELECT MAX(lon) AS max_lon, 
       MIN(lon) AS min_lon,
       MAX(lat) AS max_lat,
       MIN(lat) AS min_lat 
  FROM nodes;
~~~~

## Nodes

#### Total nodes
~~~~SQL
  SELECT COUNT(*) 
    FROM nodes;
~~~~

#### Number of Unique Users for Nodes
~~~~SQL
  SELECT COUNT(*) 
    FROM (  SELECT DISTINCT(user)
              FROM nodes) AS user_nodes;
~~~~

#### Most Popular Keys in node tags
~~~~SQL
  SELECT key, COUNT(*) 
    FROM nodes_tags 
GROUP BY key 
ORDER BY COUNT(*) DESC 
   LIMIT 15;
~~~~

#### Top Ten Contributors for nodes
~~~~SQL
  SELECT user, COUNT(*) 
    FROM nodes 
GROUP BY user 
ORDER BY COUNT(*) DESC 
   LIMIT 10;
~~~~

#### Top Ten Amenities for nodes
~~~~SQL
   SELECT value, COUNT(*) 
     FROM nodes_tags 
    WHERE key = 'amenity' 
 GROUP BY value 
 ORDER BY COUNT(*) DESC 
    LIMIT 10;
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

#### Locations with the name "Triangle"
~~~~SQL
  SELECT value 
    FROM nodes_tags 
   WHERE value LIKE '%Triangle%'
     AND key = 'name' 
ORDER BY value ASC;
~~~~

## Ways

#### Total ways
~~~~SQL
  SELECT COUNT(*) 
    FROM nodes;
~~~~

#### Number of Unique Users for Ways
~~~~SQL
  SELECT COUNT(*) 
    FROM (  SELECT DISTINCT(user)
              FROM ways) AS user_ways;
~~~~

#### Top Ten Contributors for ways
~~~~SQL
  SELECT user, COUNT(*)
    FROM ways 
GROUP BY user 
ORDER BY COUNT(*) DESC    
   LIMIT 10;
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
