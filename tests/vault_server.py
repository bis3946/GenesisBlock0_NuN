from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import Response
from tests.vault_database import init_db, insert_block

app = FastAPI()

class Block(BaseModel):
    data: str
    timestamp: str
    observer: str
    hash: str
    echo: str
    shadow: str

@app.on_event("startup")
async def startup():
    init_db()

@app.head("/vault/ingest")
async def head_ingest():
    return Response(status_code=200)

@app.post("/vault/ingest")
async def ingest(block: Block):
    insert_block(block)
    print(f"Vault sync received: {block.hash}")
    return {"status": "ok"}
