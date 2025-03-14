from fastapi import FastAPI, File, UploadFile, HTTPException
import pandas as pd

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Backend running!"}

@app.post("/solve/")
async def solve(file: UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        optimal_supplier = df.loc[df['Cost'].idxmin(), 'Supplier']
        return {
            "optimal_supplier": optimal_supplier,
            "message": f"Optimal supplier selected based on minimal cost is {optimal_supplier}"
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
