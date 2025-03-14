from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Supplier(BaseModel):
    Supplier: str
    Cost: float
    Quality: float
    DeliveryTime: float

class SupplierRequest(BaseModel):
    suppliers: List[Supplier]
    criteria: str

@app.post("/solve-json/")
def solve_supplier(request: SupplierRequest):
    criteria = request.criteria
    supplier_list = request.suppliers

    if criteria not in ["Cost", "Quality", "DeliveryTime"]:
        raise HTTPException(status_code=400, detail=f"Unsupported criteria: {criteria}")

    if criteria == "Cost":
        optimal = min(supplier_list, key=lambda x: x.Cost)
        reason = f"lowest cost ({optimal.Cost})"

    elif criteria == "Quality":
        optimal = max(supplier_list, key=lambda x: x.Quality)
        reason = f"highest quality ({optimal.Quality})"

    elif criteria == "DeliveryTime":
        optimal = min(supplier_list, key=lambda x: x.DeliveryTime)
        reason = f"shortest delivery time ({optimal.DeliveryTime} days)"

    return {
        "optimal_supplier": optimal.Supplier,
        "message": f"{optimal.Supplier} selected due to {reason}."
    }

@app.get("/")
def root():
    return {"message": "Supplier Optimisation API running!"}