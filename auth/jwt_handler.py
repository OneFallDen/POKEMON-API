import time
import jwt
from decouple import config

JWT_SECRET = config("secret")
JWT_ALGORITHM = config("algorithm")


# Function returns the generated tokens (JWTs)
def token_res(token: str):
    return{
        "access token": token
    }


# Function used to signing the JWT
def signJWT(username: str):
    payload = {
        "username": username,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_res(token)


# Function decode token and check expiring of it
def decodeJWT(token: str):
    decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return decode_token if decode_token['expires'] >= time.time() else None
