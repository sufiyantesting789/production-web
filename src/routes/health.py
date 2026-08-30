from fastapi import FastAPI

app = FastAPI()

# Expose health probe on production without authentication
@app.get("/health")
def health_check():
    return {"status": "ok", "environment": "production"}
