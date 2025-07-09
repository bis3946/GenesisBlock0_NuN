import uvicorn
from fastapi import FastAPI, Request
import json, os

app = FastAPI()
DB_FILE = "vault_db.json"

@app.post("/vault/ingest")
async def ingest_block(request: Request):
    data = await request.json()
    # append to simple JSONL db
    with open(DB_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    # CI will grep this line
    print("Vault sync received:", data.get("hash"))
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")
