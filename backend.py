from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd
from gurobipy import *

app = FastAPI(docs_url="/docs", redoc_url="/redoc")

@app.get("/")
async def root():
    return {"message": "Backend clearly practically running!"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    try:
        df = pd.read_excel(file.file)
        # Dummy optimisation logic for testing practically clearly
        optimal_supplier = df.loc[df['Cost'].idxmin(), 'Supplier']
        return {"result": f"Optimal supplier is practically exactly: {optimal_supplier}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
