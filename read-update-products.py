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
            "product_id": r[0],
            "sku": r[1],
            "name": r[2],
            "description": r[3],
            "active": r[4],
            "created_at": r[5],
            "updated_at": r[6],
        }
        for r in rows
    ]

@router.get("/products/{product_id}")
def read_product(product_id: int):
    with connect_db() as conn:
        row = conn.execute("""
            SELECT product_id, sku, name, description, active, created_at, updated_at
            FROM inventory.products
            WHERE product_id = %s
        """, (product_id,)).fetchone()

    return {
        "product_id": row[0],
        "sku": row[1],
        "name": row[2],
        "description": row[3],
        "active": row[4],
        "created_at": row[5],
        "updated_at": row[6],
    }

        