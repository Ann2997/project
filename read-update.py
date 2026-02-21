from fastapi import APIRouter

router = APIRouter()

#Replace with DB later:

persons = [{"id": 1, "name": "Alex"}]
products = [{"id": 1, "name": "Nails"}]

#Persons

@router.get("/persons")
def read_persons():
    return persons

@router.get("/persons/{person_id}")
def read_person(person_id):
    for p in persons:
        if p["id"] == person_id:
            return p

@router.put("/persons/{person_id}")
def update_person(person_id, data: dict):
    for p in persons:
        if p["id"] == person_id:
            p.update(data)
            return p
        
#Products

@router.get("/products")
def read_products():
    return products

@router.get("/products/{product_id}")
def read_product(product_id):
    for pr in products:
        if pr["id"] == product_id:
            return pr

@router.put("/products/{product_id}")
def update_product(product_id, data: dict):
    for pr in products:
        if pr["id"] == product_id:
            pr.update(data)
            return pr
