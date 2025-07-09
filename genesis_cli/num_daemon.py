import os, time, json, requests
from dotenv import load_dotenv
from genesis_code.proof_of_integrity import IntegrityNode

load_dotenv()

EXPORT_PATH = os.getenv("NUN_EXPORT_PATH", "auto_block.json")
INTERVAL = int(os.getenv("NUN_INTERVAL", 5))
OBSERVER = os.getenv("NUN_OBSERVER", "cli-daemon")
VAULT_ENDPOINT = os.getenv("NUN_VAULT_ENDPOINT", "http://localhost:8000/vault/ingest")
VAULT_TOKEN = os.getenv("NUN_VAULT_TOKEN")

def block_dict(node):
    return {
        "data": node.data,
        "timestamp": node.timestamp,
        "observer": node.observer_signature,
        "hash": node.hash,
        "echo": node.echo,
        "shadow": node.shadow
    }

headers = {}
if VAULT_TOKEN:
    headers["Authorization"] = f"Bearer {VAULT_TOKEN}"

def run_daemon():
    print(f"NuN Daemon → every {INTERVAL}s, endpoint={VAULT_ENDPOINT}, token={'set' if VAULT_TOKEN else 'none'}")
    while True:
        node = IntegrityNode(data="AutoBlock", observer_signature=OBSERVER)
        blk = block_dict(node)
        with open(EXPORT_PATH, "w") as f:
            json.dump(blk, f, indent=2)
        try:
            r = requests.post(VAULT_ENDPOINT, json=blk, headers=headers, timeout=3)
            print("Vault sync status:", r.status_code)
        except Exception as e:
            print("Vault sync error:", e)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_daemon()
