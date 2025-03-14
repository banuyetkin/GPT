

from fastapi import FastAPI, File, UploadFile
import pandas as pd
from gurobipy import *

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend Running"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)
    # Your optimization

