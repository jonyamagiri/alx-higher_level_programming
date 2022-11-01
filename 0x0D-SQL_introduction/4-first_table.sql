-- Creates a table called first_table in the current database in MySQL server.
-- database name passed as argument of mysql command.
-- first_table has id (INT), name (VARCHAR(256))
-- if table exists, script should not fail. No SELECT or SHOW statements.

CREATE TABLE IF NOT EXISTS first_table (id INT, name VARCHAR(256));
