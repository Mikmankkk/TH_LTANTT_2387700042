from jwt_validator.validator import JWTValidator
import jwt
import datetime
import os

def generate_token(sign_key):
    payload = {"sub": "test", "exp": datetime.datetime.now(datetime.timezone.utc)
               + datetime.timedelta(minutes=5)}
    return jwt.encode(payload, sign_key, algorithm="HS256")

def test_valid_token():
    valid_key = os.getenv("VALID_KEY", "secret123")
    token = generate_token(valid_key)
    validator = JWTValidator(valid_key)
    result = validator.validate(token)
    assert result["valid"] is True
    assert result["payload"]["sub"] == "test"

def test_invalid_signature():
    token = generate_token("wrongkey")
    validator = JWTValidator("correctkey")
    result = validator.validate(token)
    assert result["valid"] is False
