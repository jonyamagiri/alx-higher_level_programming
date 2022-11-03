-- Creates the table unique_id in database hbtn_0d_2
-- unique_id has id INT with the default value 1 and must be unique; name VARCHAR(256)
-- if table unique_id already exists, script should not fail
-- database name passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS unique_id(
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
