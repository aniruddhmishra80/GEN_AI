from fastapi import FastAPI, HTTPException
from models import product

app = FastAPI()


products = [
    product(id=1, name="phone", discription="Android", price=99, quantity=20),
    product(id=2, name="laptop", discription="Windows", price=199, quantity=10),
]


@app.get("/")
def greet():
    return {"message": "hello greetings"}


@app.get("/products")
def get_all_product_details():
    return products


@app.get("/products/{id}")
def get_all_products_byid(id: int):
    for item in products:
        if item.id == id:
            return item
    raise HTTPException(status_code=404, detail="Product not found")


@app.post("/product", status_code=201)
def add_product(payload: product):
    products.append(payload)
    return payload


@app.put("/products/{id}")
def update_products(id: int, payload: product):
    for i, item in enumerate(products):
        if item.id == id:
            products[i] = payload
            return {"message": "Product updated successfully"}
    raise HTTPException(status_code=404, detail="No product found")


@app.delete("/product/{id}")
def delete_product(id: int):
    for i in range(len(products)):
        if products[i].id == id:
            products.pop(i)
            return {"message": "Product deleted successfully"}
    return "Product not found"