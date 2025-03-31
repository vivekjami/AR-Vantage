from fastapi import FastAPI

app = FastAPI(title="AR-Vantage API", version="1.0")

@app.get("/")
def root():
    return {"message": "Welcome to AR-Vantage"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
