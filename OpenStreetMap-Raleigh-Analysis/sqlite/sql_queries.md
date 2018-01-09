# SQL Queries 

This file holds all of the different queries done on the database. Not all are included in the final report.
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
  FROM (  SELECT user, COUNT(*) AS num
            FROM nodes
        GROUP BY user

           UNION

          SELECT user, COUNT(*) AS num
            FROM ways
        GROUP BY user) AS total_users;
~~~~

#### Top Five Contributors
~~~~SQL
  SELECT user, num
    FROM (  SELECT user, COUNT(*) AS num
              FROM nodes
          GROUP BY user

             UNION

            SELECT user, COUNT(*) AS num
              FROM ways
          GROUP BY user) AS total_users 
ORDER BY num DESC
   LIMIT 5;
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
    FROM (  SELECT user, COUNT(*) AS num
              FROM nodes 
          GROUP BY user 
          ORDER BY num DESC) AS user_nodes;
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
ORDER BY COUNT(*) DESC,
   LIMIT 10;
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
    FROM (  SELECT user, COUNT(*) AS num
              FROM ways 
          GROUP BY user 
          ORDER BY num DESC) AS user_ways;
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
   LIMIT 10;
~~~~
