CREATE TABLE flights (
id INTEGER PRIMARY KEY AUTOINCREMENT,
origin TEXT NOT NULL,
destination TEXT NOT NULL,
duration INTEGER NOT NULL);

SELECT * FROM flights;

INSERT INTO flights (origin, destination, duration) VALUES 
("New York", "London", 415);

INSERT INTO flights (origin, destination, duration) VALUES
("Shanghai", "Paris", 760),
("Istanbul", "Tokyo", 700),
("New York", "Paris", 435),
("Moscow", "Paris", 245),
("Lima", "New York", 455);


SELECT * FROM flights WHERE origin="New York";

SELECT * FROM flights WHERE duration > 500 AND destination="Paris";
SELECT * FROM flights WHERE duration > 500 OR destination="Paris";

SELECT * FROM flights WHERE origin IN ("New York", "Lima");

SELECT * FROM flights WHERE origin LIKE "%a%"; 
/* 
'%' represents any character of any length
e.g. finds flights where there is the letter a in origin
*/

UPDATE flights SET duration = 430 WHERE origin="New York" AND destination="Paris";
-- updates flight duration to 430 if origin is NY and destination is Paris

DELETE FROM flights WHERE destination="Tokyo";
-- deletes flights where the destination is Tokyo

