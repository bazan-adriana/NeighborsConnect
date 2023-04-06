SELECT * FROM project_schema.users;
SELECT * FROM users;
SELECT * FROM posts;
SELECT * FROM addresses;
SELECT * FROM posts;

SELECT * FROM users
JOIN posts ON users.id = posts.user_id
JOIN addresses ON posts.address_id = addresses.id;


INSERT INTO posts (name, descriptions, comments, date, currentmonth, user_id, address_id)
VALUES ('Potluck', 'At the pool area!', 'Attends is optional', '2023-10-20', 1, 1,1);

INSERT INTO users (first_name, last_name, email, password)
VALUES ('Andy', 'Kills', 'a@.isoptional', 'password');



SELECT * FROM posts
JOIN usersON posts.user_id = users.id
JOIN addresses ON addresses.id = posts.address_id
WHERE posts.id = 2;

SELECT * FROM posts
WHERE posts.id = 3;






INSERT INTO addresses (street, city, state)
VALUES ('321street', 'San Francisco', 'CA');

SELECT * FROM addresses
JOIN users
ON addresses.user_id = users.id;


SELECT * FROM posts
JOIN posts ON users.id = posts.user_id
LEFT JOIN addresses as address ON address.id = posts.user_id
WHERE users.id = 1;

SELECT * FROM posts
JOIN addresses
ON addresses_id = addresses.id
WHERE users.id = 1;

DELETE FROM posts WHERE posts.user_id = 1;