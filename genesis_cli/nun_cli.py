#!/usr/bin/env python3
import argparse
import json
from genesis_code.proof_of_integrity import IntegrityNode

def main():
    parser = argparse.ArgumentParser(description="NuN CLI – Genesis Block 0 Tool")
    parser.add_argument("data", help="Data to encode into the Integrity Block")
    parser.add_argument("--observer", default="ψ-bis3946", help="Observer signature")
    parser.add_argument("--export", metavar="FILENAME", help="Export block to .json")
    parser.add_argument("--hash-only", action="store_true", help="Output only hash")
    parser.add_argument("--silent", action="store_true", help="Suppress verbose output")
    args = parser.parse_args()

    node = IntegrityNode(data=args.data, observer_signature=args.observer)

    if not args.silent:
        print("🔮 Integrity Block Created")
        print(f"Hash: {node.hash}")
        print(f"Echo: {node.echo}")
        print(f"Shadow: {node.shadow}")

    if args.hash_only:
        print(node.hash)

    if args.export:
        export_data = {
            "data": node.data,
            "timestamp": node.timestamp,
            "observer": node.observer_signature,
            "hash": node.hash,
            "echo": node.echo,
            "shadow": node.shadow
        }
        with open(args.export, "w") as f:
            json.dump(export_data, f, indent=2)
        if not args.silent:
            print(f"✅ Block exported to {args.export}")

if __name__ == "__main__":
    main()
