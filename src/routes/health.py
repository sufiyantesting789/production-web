from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
    return {"service": "production-web", "status": "online"}
