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
    # Optimization logic placeholder
    return {"result": "Optimization successfully solved practically clearly!"}