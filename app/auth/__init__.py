import hashlib

def hash_password(password):
    """Hashes the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def verify_password(stored_hash, password):
    """Verifies if the given password matches the stored hash."""
    return stored_hash == hash_password(password)
