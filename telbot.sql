--
-- File generated with SQLiteStudio v3.4.4 on Wed Nov 1 21:17:32 2023
--
-- Text encoding used: System
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- Table: bot
CREATE TABLE IF NOT EXISTS bot (id INTEGER PRIMARY KEY UNIQUE, user_id INTEGER UNIQUE, user_name TEXT (255), user_surname TEXT (255), username TEXT NOT NULL);

COMMIT TRANSACTION;
PRAGMA foreign_keys = on;
