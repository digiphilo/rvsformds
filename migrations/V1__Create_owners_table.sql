CREATE TABLE owners (
 id SERIAL PRIMARY KEY,
 name VARCHAR,
 email VARCHAR,
 phone VARCHAR,
 city VARCHAR,
 state VARCHAR,
 county VARCHAR,
 zip VARCHAR,
 rvtype VARCHAR,
 other VARCHAR,
 matched BOOLEAN
);
