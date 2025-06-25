CREATE DATABASE grocery_store;

USE grocery_store

CREATE TABLE Products (
Product_id INT AUTO_INCREMENT PRIMARY KEY,
Product_Name VARCHAR(50),
Category VARCHAR(50),
Price DECIMAL(10,2),
Stock INT
);

CREATE TABLE Sales (
Sale_id INT AUTO_INCREMENT PRIMARY KEY,
Product_id INT,
Quantity INT,
Total_Price DECIMAL(10,2),
Sale_Date DATE,
FOREIGN KEY (Product_id) REFERENCES Products (Product_id)
);

INSERT INTO Products ( Product_Name, Category, Price, Stock) VALUES
('Apples','Fruits',250,100),
('Milk','Dairy',50,30),
('Bread','Bakery',20,10),
('Eggs','Dairy',7,100),
('Tomatoes','Vegetables',30,200);