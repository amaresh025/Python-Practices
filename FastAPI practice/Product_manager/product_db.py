import mysql.connector
from modle import Product
from dotenv import load_dotenv
import os 
load_dotenv()

conn = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)

cur = conn.cursor(dictionary=True)

def all_products():
    cur.execute("SELECT * FROM product")
    return cur.fetchall()

def add_product(product: Product):
   
    querry = ("""INSERT INTO product (name, price, stocks) 
              VALUES 
              (%s, %s, %s)
            """)
    cur.execute(querry, (product.name, product.price, product.stocks))
    conn.commit()
    new_id = cur.lastrowid

    return {"message": "Product Added",
            "id": new_id}

def Update_product(product: Product):
    querry = ("""UPDATE product
              SET name = %s,
              price = %s,
              stocks = %s
              WHERE id = %s""")
    cur.execute(querry, (product.name, product.price, product.stocks, product.id))
    conn.commit()
    return {"message": "Update Success"}

def delete_product(product_id: int):
    querry = ("""DELETE FROM product 
              WHERE id = %s""")
    cur.execute(querry, (product_id,))
    conn.commit()
    return {"message": "Delete Success"}

cur.execute("SELECT * FROM product")
print(cur.fetchall())
