import time, json
from datetime import datetime
from genesis_code.proof_of_integrity import IntegrityNode

def run_daemon(export_path="auto_block.json", interval=30, observer="ψ-bis3946-daemon"):
    print(f"[{datetime.now()}] 🔁 NuN Daemon started – block every {interval}s")
    while True:
        data = f"AutoBlock @ {datetime.utcnow().isoformat()}"
        node = IntegrityNode(data, observer)
        export_data = {
            "data": node.data,
            "timestamp": node.timestamp,
            "observer": node.observer_signature,
            "hash": node.hash,
            "echo": node.echo,
            "shadow": node.shadow
        }
        with open(export_path, "w") as f:
            json.dump(export_data, f, indent=2)
        print(f"[{datetime.now()}] ✅ Block exported to {export_path}")
        time.sleep(interval)
