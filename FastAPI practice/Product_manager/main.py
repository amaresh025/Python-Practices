from fastapi import FastAPI, HTTPException
from modle import Product
import product_db as p
import mysql.connector

app = FastAPI()

@app.get("/")
def products():
    return p.all_products()

@app.post("/products")
def add(product:Product):
    try:
        return p.add_product(product)

    except mysql.connector.Error as e:
        p.conn.rollback()
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")
    
@app.put("/products/{product_id}")

def update(product_id : int, product: Product):
    try:
        product.id = product_id
        result = p.Update_product(product)
        if result is None:
            raise HTTPException(status_code=404, detail="Product not found")
        return result
    
    except mysql.connector.Error as e:
        p.conn.rollback()
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")

@app.delete("/products/{product_id}")
def delete(product_id : int):
    try:
        result = p.delete_product(product_id)
        
        if result is None:
            raise HTTPException(status_code=404, detail="Product not found")
        
        return result
    except mysql.connector.Error as e:
        p.conn.rollback()
        raise HTTPException(status_code=500, detail=f"DB error: {str(e)}")
    