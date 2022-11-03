-- Creates the database hbtn_0d_usa and the table cities (in the database hbtn_0d_usa)
-- cities has id INT unique, auto generated, can’t be null and is a primary key
-- state_id INT, can’t be null and must be a FOREIGN KEY that references to id of the states table, name VARCHAR(256) can’t be null
-- if database hbtn_0d_usa already exists, script should not fail
-- if table cities already exists, script should not fail

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS cities(
    PRIMARY KEY(id),
    id INT UNIQUE AUTO_INCREMENT NOT NULL,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    FOREIGN KEY(state_id) REFERENCES hbtn_0d_usa.states(id)
);
