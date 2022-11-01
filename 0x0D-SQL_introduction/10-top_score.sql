-- Lists all records of the table second_table of the database hbtn_0c_0
-- display both the score and the name (in this order)
-- Records should be ordered by score (top first)
-- database name passed as argument of mysql command

SELECT score, name
FROM second_table
ORDER BY score DESC;
