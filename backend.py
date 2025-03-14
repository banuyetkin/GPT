from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Supplier(BaseModel):
    Supplier: str
    Cost: float
    Quality: float
    DeliveryTime: int

class SupplierRequest(BaseModel):
    suppliers: List[Supplier]
    criteria: str

@app.post("/solve-json/")
def solve_supplier(request: SupplierRequest):
    if request.criteria == "minimum cost":
        optimal = min(request.suppliers, key=lambda x: x.Cost)
        return {
            "optimal_supplier": optimal.Supplier,
            "message": f"{optimal.Supplier} selected based on minimum cost (${optimal.Cost})."
        }
    return {"message": "Unsupported criteria."}
