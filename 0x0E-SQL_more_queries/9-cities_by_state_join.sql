-- Lists all cities contained in the database hbtn_0d_usa
-- display: cities.id - cities.name - states.name
-- sorted in ascending order by cities.id; use only one SELECT statement

SELECT cities.id, cities.name, states.name
FROM cities
JOIN states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
