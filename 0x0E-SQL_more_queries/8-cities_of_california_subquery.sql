-- Lists all the cities of California that can be found in the database hbtn_0d_usa
-- states table contains only one record where name = California (but the id can be different)
-- sorted in ascending order by cities.id; No JOIN keyword

SELECT id, name
FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = "California")
ORDER BY id ASC;
