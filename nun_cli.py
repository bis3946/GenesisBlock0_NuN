#!/usr/bin/env python3
import argparse
from code.proof_of_integrity import IntegrityNode

def main():
    parser = argparse.ArgumentParser(description="NuN CLI – Genesis Block 0 Tool")
    parser.add_argument("data", help="Data to encode into the Integrity Block")
    parser.add_argument("--observer", default="ψ-bis3946", help="Observer signature")
    args = parser.parse_args()

    print("🔮 Generating Integrity Block...")
    node = IntegrityNode(data=args.data, observer_signature=args.observer)

    print(f"Hash: {node.hash}")
    print(f"Echo: {node.echo}")
    print(f"Shadow: {node.shadow}")

if __name__ == "__main__":
    main()
