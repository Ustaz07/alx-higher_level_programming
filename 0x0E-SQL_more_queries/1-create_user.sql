-- SQL script to create MySQL user user_0d_1 with all privileges

-- Check if user_0d_1 already exists
SELECT user FROM mysql.user WHERE user = 'user_0d_1';

-- If user_0d_1 does not exist, create the user and grant all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
