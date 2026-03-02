from fastapi import FastAPI

app = FastAPI(title="Structa API")

@app.get("/")
def health_check():
    return {
        "status": "ok"
    }