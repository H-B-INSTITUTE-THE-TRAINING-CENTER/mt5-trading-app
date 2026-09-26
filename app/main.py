from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "message":"MT5 Trading App API is running"
    }

@app.get("/health")
def health():
    return{
        "status":"healthy"
    }