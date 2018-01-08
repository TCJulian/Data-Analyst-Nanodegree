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

