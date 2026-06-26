DROP DATABASE IF EXISTS lesson14;

CREATE DATABASE lesson14;

USE lesson14;

CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50),
    password VARCHAR(50),
    email VARCHAR(100)
);

CREATE TABLE seller (
    id INT AUTO_INCREMENT PRIMARY KEY,
    company VARCHAR(100),
    phone VARCHAR(20)
);

CREATE TABLE products (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    cost INT,
    count INT,
    seller_id INT,
    FOREIGN KEY (seller_id) REFERENCES seller(id)
);

CREATE TABLE orders (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    product_id INT,
    count INT,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (product_id) REFERENCES products(id)
);

INSERT INTO users (username, password, email) VALUES
('ivan', '1234', 'ivan@mail.com'),
('anna', '5678', 'anna@mail.com');

INSERT INTO seller (company, phone) VALUES
('Apple', '111-111'),
('Samsung', '222-222');

INSERT INTO products (name, cost, count, seller_id) VALUES
('iPhone', 1000, 5, 1),
('Galaxy', 900, 10, 2);

INSERT INTO orders (user_id, product_id, count) VALUES
(1, 1, 1),
(2, 2, 2);

SELECT * FROM users;
SELECT * FROM seller;
SELECT * FROM products;
SELECT * FROM orders;