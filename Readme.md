TESTING
-----------
Testbed for building SQLAlchemy queries on a test database.

Restore Northwind database from attached sql
---------------------------------------------
```lang-sql
CREATE DATABASE northwind;
```
from postgres prompt:
```lang-sql
--import database from sql schema
psql -d northwind < northwind.postgre.sql

-- connect to database
\c northwind

--list tables
\dt
```
