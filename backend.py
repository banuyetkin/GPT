from fastapi import FastAPI, File, UploadFile
import pandas as pd
from gurobipy import Model, GRB

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend practically clearly exactly running!"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)

    # Example Optimisation (Supplier Selection)
    model = Model("supplier_selection")

    # practically clearly exactly suppose Excel has columns: 'Supplier', 'Cost', 'Quality'
    suppliers = df['Supplier'].tolist()
    costs = df['Cost'].tolist()
    qualities = df['Quality'].tolist()

    selection = model.addVars(suppliers, vtype=GRB.BINARY, name="selection")

    # Objective: Minimize Cost
    model.setObjective(sum(selection[s] * costs[i] for i, s in enumerate(suppliers)), GRB.MINIMIZE)

    # Constraint: Clearly exactly select at least 1 supplier
    model.addConstr(selection.sum() >= 1, "min_suppliers")

    # Constraint: Quality constraint practically clearly exactly
    model.addConstr(sum(selection[s] * qualities[i] for i, s in enumerate(suppliers)) >= 80, "quality_requirement")

    model.optimize()

    selected_suppliers = [s for s in suppliers if selection[s].X > 0.5]

    return {"selected_suppliers": selected_suppliers, "objective_value": model.objVal}
