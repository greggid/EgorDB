CREATE TABLE users (
id serial PRIMARY KEY,
username TEXT NOT NULL, 
fullname TEXT NOT NULL,
password TEXT NOT NULL,	
email TEXT, 
created_on TIMESTAMP, 
last_login TIMESTAMP, 
ilovecookie TEXT);

