import uvicorn, os, json
from fastapi import FastAPI, Request, HTTPException
from starlette.status import HTTP_401_UNAUTHORIZED

app = FastAPI()
DB_FILE = "vault_db.json"
EXPECTED = os.getenv("NUN_VAULT_TOKEN", "secret-token")

@app.post("/vault/ingest")
async def ingest(request: Request):
    auth = request.headers.get("Authorization")
    if not auth or auth != f"Bearer {EXPECTED}":
        raise HTTPException(status_code=HTTP_401_UNAUTHORIZED, detail="Invalid token")
    data = await request.json()
    with open(DB_FILE, "a") as f:
        f.write(json.dumps(data) + "\n")
    print("Vault sync received:", data.get("hash"))
    return {"status": "ok"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
