from genesis_code.proof_of_integrity import IntegrityNode

print("🧪 Running Genesis Block 0 Integrity Demo...")

data = "This is a test block from Root Authority"
observer = "ψ-bis3946"

node = IntegrityNode(data, observer)
print("🔐 Block Created:")
print(node)
print(f"Hash: {node.hash}")
print(f"Echo: {node.echo}")
print(f"Shadow: {node.shadow}")
