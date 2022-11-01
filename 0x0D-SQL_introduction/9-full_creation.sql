-- Creates table second_table in database hbtn_0c_0 and adds multiples rows.
-- second_table has id INT, name VARCHAR(256) and score INT
-- database name passed as argument of mysql command
-- if second_table exists, script should not fail. No SELECT and SHOW statements

CREATE TABLE IF NOT EXISTS second_table (
    id INT, 
    name VARCHAR(256),
    score INT);
INSERT INTO second_table (id, name, score) VALUES
    (1, 'John', 10),
    (2, 'Alex', 3),
    (3, 'Bob', 14),
    (4, 'George', 8);
