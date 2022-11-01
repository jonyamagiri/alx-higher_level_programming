-- Lists all records of second_table of database hbtn_0c_0
-- no listing of rows without a name value
-- display the score and the name (in this order); listed by descending score
-- database name passed as argument of mysql command

SELECT score, name
FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
