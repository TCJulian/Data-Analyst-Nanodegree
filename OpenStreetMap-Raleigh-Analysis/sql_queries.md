## Count Number of Unique Users

SELECT COUNT(*) FROM (SELECT user, COUNT(*) FROM nodes GROUP BY user ORDER BY COUNT(*) DESC) as subquery;
