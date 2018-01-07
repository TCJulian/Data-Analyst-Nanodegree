#### Count Number of Unique Users
~~~~SQL
  SELECT COUNT(*) 
    FROM (  SELECT user, COUNT(*)
              FROM nodes 
          GROUP BY user 
          ORDER BY COUNT(*) DESC) AS subquery;
~~~~

#### Show Top Ten Contributors
~~~~SQL
  SELECT user, COUNT(*) 
    FROM nodes 
GROUP BY user 
ORDER BY COUNT(*) DESC 
   LIMIT 10;
~~~~
