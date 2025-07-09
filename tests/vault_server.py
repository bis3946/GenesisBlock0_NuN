from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Block(BaseModel):
    data: str
    timestamp: str
    observer: str
    hash: str
    echo: str
    shadow: str

@app.post("/vault/ingest")
async def ingest(block: Block):
    print(f"Vault sync received: {block.hash}")
    return {"status": "ok"}
