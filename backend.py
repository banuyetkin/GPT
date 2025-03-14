from fastapi import FastAPI, File, UploadFile
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend running!"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    df = pd.read_excel(file.file)
    optimal_supplier = df.loc[df['Cost'].idxmin(), 'Supplier']
    return {"optimal_supplier": optimal_supplier}
