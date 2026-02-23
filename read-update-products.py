from fastapi import APIRouter
from inventory_alerts.db import connect_db

router = APIRouter()

#Products

@router.get("/products")
def read_products():
    with connect_db() as conn:
        rows = conn.execute("""
            SELECT product_id, sku, name, description, active, created_at, updated_at
            FROM inventory.products
            ORDER BY product_id
        """).fetchall()
    
    return [
        {
            "product_id"
            "sku"
            "name"
            "description"
            "active"
            "created_at"
            "updated_at"
        }
        for r in rows
    ]
        