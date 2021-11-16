-- Change collation in database
ALTER DATABASE hbtn_0c_0
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Change collation in table
ALTER TABLE hbtn_0c_0.first_table
CONVERT TO CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

-- Change collation in field
ALTER TABLE hbtn_0c_0.first_table
MODIFY name VARCHAR(256)
COLLATE utf8mb4_unicode_ci;
