from modle import Product

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return "you are on the right spot"
@app.get("/home")
def root():
    return {"status": "everything is ok"}

products = [
    Product(id = 1, name = "laptop", price = 44000),
    Product(id = 2, name = "phone", price = 14000)
]
@app.get("/products")

def get_product():
    return products


@app.post("/product")
def add_products(product : Product):
    products.append(product)
    return products