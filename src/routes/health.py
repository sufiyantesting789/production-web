from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def index():
    return {"service": "production-web", "status": "online"}
@app.get("/health")
def staging_health():
    # Unauthenticated probe for staging
    return {"status": "healthy", "env": "staging"}
