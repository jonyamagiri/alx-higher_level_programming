-- Creates the MySQL server user user_0d_1
-- user_0d_1 has all privileges, with password set to user_0d_1_pwd
-- if user user_0d_1 already exists, script should not fail

CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_pwd'; GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
FLUSH PRIVILEGES;
