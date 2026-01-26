from modle import Product
from fastapi import HTTPException
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "you are on the right spot"
@app.get("/home")
def root():
    return {"status": "everything is ok"}

products = [
    Product(id = 1, name = "laptop"),
    Product(id = 2, name = "phone", price = 14000)
]
@app.get("/products/{id}")

def get_product(id : int):
    for item in range(len(products)):
        if products[item].id == id:
            return products[item]
    raise HTTPException(
        status_code=404,
        detail="product not found" 
    )

    

@app.post("/product")
def add_products(product : Product):
    products.append(product)
    return products
