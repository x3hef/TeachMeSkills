import hashlib
import secrets

ITERATIONS = 600_000


def hash_password(password: str) -> str:
    salt = secrets.token_hex(16)
    password_hash = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode("utf-8"),
        salt.encode("utf-8"),
        ITERATIONS,
    ).hex()
    return f"{salt}${password_hash}"


def generate_api_token() -> str:
    return secrets.token_urlsafe(32)
