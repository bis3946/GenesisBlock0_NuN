import os, time, json, requests
from dotenv import load_dotenv
from genesis_code.proof_of_integrity import IntegrityNode

load_dotenv()

EXPORT_PATH = os.getenv("NUN_EXPORT_PATH", "auto_block.json")
INTERVAL = int(os.getenv("NUN_INTERVAL", 5))
OBSERVER = os.getenv("NUN_OBSERVER", "cli-daemon")
VAULT_ENDPOINT = os.getenv("NUN_VAULT_ENDPOINT", "http://localhost:8000/vault/ingest")

def run_daemon():
    print(f"NuN Daemon started – every {INTERVAL}s, endpoint={VAULT_ENDPOINT}")
    while True:
        node = IntegrityNode(data="AutoBlock", observer_signature=OBSERVER)
        with open(EXPORT_PATH, "w") as f:
            json.dump(node.as_dict(), f, indent=2)
        try:
            r = requests.post(VAULT_ENDPOINT, json=node.as_dict(), timeout=3)
            print("Vault sync status:", r.status_code)
        except Exception as e:
            print("Vault sync error:", e)
        time.sleep(INTERVAL)

if __name__ == "__main__":
    run_daemon()
