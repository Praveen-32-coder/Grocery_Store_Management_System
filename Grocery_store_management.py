import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt

#Connect to MySQL
conn = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    password = 'Praveen@@8',
    database = 'grocery_store'
)
cursor = conn.cursor()

#Record a sale sample
cursor.execute('INSERT INTO sales (product_id, quantity,total_price,sale_date) VALUES (%s, %s, %s, CURDATE())',(1,5,250*3))
conn.commit()

#Fetch stock data

cursor.execute('SELECT Product_name,category,price,stock FROM Products')
rows = cursor.fetchall()

df = pd.DataFrame(rows,columns=['Product','Category','Price','Stock'])
print(df)

#Plot stock bar chart
plt.figure(figsize=(10,6))
plt.bar(df['Product'],df['Stock'],color = 'orange')
plt.xlabel('Product')
plt.ylabel('Stock Quantity')
plt.title('Current Sock in Grocery Store')
plt.tight_layout()
plt.savefig('mysql_grocery_store_stock.png')
plt.show()

cursor.close()
conn.close()