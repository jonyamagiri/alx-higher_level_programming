-- Lists all records with score >= 10 in second_table of database hbtn_0c_0
-- display both the score and the name (in this order)
-- records ordered by score (top first)
-- database name passed as argument of mysql command

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
