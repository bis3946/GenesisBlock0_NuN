import hashlib
from datetime import datetime

class IntegrityNode:
    def __init__(self, data, observer_signature):
        self.data = data
        self.timestamp = datetime.utcnow().isoformat()
        self.observer_signature = observer_signature
        self.hash = self.compute_hash()
        self.echo = self.create_echo()
        self.shadow = self.create_shadow()
        self.status = "VERIFIED"

    def compute_hash(self):
        data_string = f"{self.data}|{self.timestamp}|{self.observer_signature}"
        return hashlib.sha3_512(data_string.encode()).hexdigest()

    def create_echo(self):
        return hashlib.blake2b((self.hash + "echo").encode()).hexdigest()

    def create_shadow(self):
        entropy_signature = hashlib.sha256(self.hash.encode()).hexdigest()
        return hashlib.md5((entropy_signature + "shadow").encode()).hexdigest()

    def validate_integrity(self, check_hash):
        return self.hash == check_hash

    def __repr__(self):
        return f"<VaultNode IntegrityHash={self.hash[:10]}... Status={self.status}>"
