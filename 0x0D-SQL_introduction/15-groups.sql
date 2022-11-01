-- Lists number of records with same score in second_table of database hbtn_0c_0
-- display score, number of records for the score with label number
-- sorted by the number of records (descending)
-- database name passed as argument of mysql command

SELECT score, COUNT(score) AS 'number'
FROM second_table
GROUP BY score
ORDER BY number DESC;
