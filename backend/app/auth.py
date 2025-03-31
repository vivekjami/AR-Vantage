import jwt
from datetime import datetime, timedelta

SECRET_KEY = "supersecurekey"
ALGORITHM = "HS256"

def create_jwt(data: dict, expires_delta: timedelta):
    data.update({"exp": datetime.utcnow() + expires_delta})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
