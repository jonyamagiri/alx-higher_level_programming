-- Creates the table force_name in database hbtn_0d_2
-- force_name has id INT, name VARCHAR(256) can’t be null
-- if table force_name already exists, script should not fail
-- database name passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS force_name(
    id INT,
    name VARCHAR(256) NOT NULL
);
