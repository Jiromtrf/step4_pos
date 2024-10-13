from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

app = FastAPI()

# CORS 設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 必要に応じて ["http://localhost:3000"] などに制限
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 以下、商品検索エンドポイントのコード
class PurchaseItem(BaseModel):
    code: str
    quantity: int

class PurchaseRequest(BaseModel):
    items: List[PurchaseItem]

products_db = {
    "4902102111513": {"name": "ペプシコーラ", "price": 140},
    "1234567890123": {"name": "おーいお茶", "price": 150}
}

@app.get("/search_product/{code}")
async def search_product(code: str):
    product = products_db.get(code)
    if product:
        return {"name": product["name"], "price": product["price"]}
    return {"error": "Product not found"}

@app.post("/purchase")
async def purchase(request: PurchaseRequest):
    total_amount = 0
    for item in request.items:
        product = products_db.get(item.code)
        if product:
            total_amount += product["price"] * item.quantity
    return {"success": True, "total_amount": total_amount}
