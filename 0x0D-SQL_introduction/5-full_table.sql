-- Script to print the full description of the table first_tablefrom the database hbtn_0c_0

-- Define the database name
SET @database_name = 'hbtn_0c_0';

-- Get the table information from INFORMATION_SCHEMA
SELECT COLUMN_NAME, COLUMN_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = @database_name
AND TABLE_NAME = 'first_table';
