-- Creates the database hbtn_0d_usa and the table states (in the database hbtn_0d_usa)
-- states has id INT unique, auto generated, can’t be null and is a primary key; name VARCHAR(256) can’t be null
-- if database hbtn_0d_usa already exists, script should not fail
-- if table states already exists, script should not fail
-- database name passed as an argument of the mysql command

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(
    PRIMARY KEY(id),
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    name VARCHAR(256) NOT NULL
);
