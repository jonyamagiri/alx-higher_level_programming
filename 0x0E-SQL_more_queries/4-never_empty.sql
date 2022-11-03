-- Creates the table id_not_null in database hbtn_0d_2
-- id_not_null has id INT with the default value 1, name VARCHAR(256)
-- if table id_not_null already exists, script should not fail
-- database name passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS id_not_null(
    id INT DEFAULT 1,
    name VARCHAR(256)
);
