-- Removes all records with score <= 5 in second_table of database hbtn_0c_0
-- database name passed as argument of mysql command

UPDATE second_table
SET score = 10
WHERE name = 'Bob'












-- Removes all records with a score <= 5 in the table second_table.
DELETE FROM `second_table`
WHERE `score` <= 5;





