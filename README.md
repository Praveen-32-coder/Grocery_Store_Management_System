# Grocery_Store_Management_System
This project is a simple yet functional Grocery Store Management System  buit using Python for backend logic and MySQL for database management. It helps track inventory, record sales, and visualize current stock using charts.


# 🛒 Grocery Store Management System (Python + MySQL)

A simple Grocery Store Management System built using **Python**, **MySQL**, and **Matplotlib**. This project allows you to manage products and sales in a grocery store database, and visualize the current stock using a bar chart.

## 📁 Project Structure

- `Grocery_management_project.sql` – SQL script to create and populate the database and tables.
- `Grocery_store_management.py` – Python script to:
  - Connect to MySQL database
  - Insert a sample sales record
  - Fetch and display product stock
  - Visualize stock levels using a bar chart

## 💡 Features

- Create and manage a MySQL database for grocery products and sales.
- Insert real-time sales transactions.
- Display current stock levels of all products.
- Generate and show a bar chart of product stock using Matplotlib.

## 🧰 Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python`
- Pandas
- Matplotlib

## 🛠️ How to Run

### 1. Setup MySQL Database

1. Make sure MySQL server is running.
2. Open a MySQL client or workbench.
3. Run the SQL script:
   ```sql
   SOURCE path/to/Grocery_management_project.sql;

# Install Required Python Libraries
pip install mysql-connector-python, pandas, matplotlib

# Run the Python Script
python Grocery_store_management.py

# Output
A new sales record will be inserted.

The current stock of products will be printed in the console.

A bar chart (mysql_grocery_store_stock.png) showing the stock will be displayed and saved.

# Sample Output
    Product  Category  Price  Stock
0   Apples     Fruits  250.0    100
1     Milk      Dairy   50.0     30
2    Bread     Bakery   20.0     10
3     Eggs      Dairy    7.0    100
4 Tomatoes Vegetables   30.0    200
