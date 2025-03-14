from fastapi import FastAPI, File, UploadFile
import pandas as pd
from gurobipy import *

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

@app.get("/")
async def root():
    return {"message": "Backend clearly practically running!"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)

    # Example optimisation using Gurobi
    model = Model("Supplier Selection")

    # Assume Excel has columns: 'Supplier', 'Cost', 'Quality', 'DeliveryTime'
    suppliers = df["Supplier"].tolist()
    costs = df["Cost"].tolist()
    quality = df["Quality"].tolist()
    delivery = df["DeliveryTime"].tolist()

    x = model.addVars(suppliers, vtype=GRB.BINARY, name="select_supplier")

    # Example constraint: choose exactly 2 suppliers
    model.addConstr(x.sum() == 2)

    # Objective example: Minimize cost while maximizing quality
    model.setObjective(quicksum(costs[i] * x[suppliers[i]] for i in range(len(suppliers))) 
                       - quicksum(quality[i] * x[suppliers[i]] for i in range(len(suppliers))),
                       GRB.MINIMIZE)

    model.optimize()

    selected_suppliers = [supplier for supplier in suppliers if x[supplier].X > 0.5]

    return {"Selected Suppliers": selected_suppliers}
