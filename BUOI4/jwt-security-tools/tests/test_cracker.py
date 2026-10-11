from jwt_cracker.cracker import JWTCracker
import jwt
import tempfile
import os

def test_crack_token():
    target_secret = os.getenv("TARGET_SECRET", "supersecret")
    token = jwt.encode({"sub": "test"}, target_secret, algorithm="HS256")

    with tempfile.NamedTemporaryFile(mode="w+", delete=False) as f:
        f.write(f"wrongpass\n123456\n{target_secret}\n")
        f.seek(0)
        cracker = JWTCracker(token, f.name)
        found = cracker.crack()

    assert found == target_secret
