-- Updates the score of Bob to 10 in the table second_table
-- no use of Bob’s id value, only the name field
-- database name passed as argument of mysql command

UPDATE second_table
SET score = 10
WHERE name = 'Bob';
