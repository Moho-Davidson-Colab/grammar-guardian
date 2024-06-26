from pydantic import BaseModel, Field
import uuid
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone
from flask import current_app as app
from dotenv import load_dotenv
load_dotenv()


class User(BaseModel):
    # userId: uuid = Field(default=uuid.uuid4(), alias="_id")
    username: str = Field(...)
    password: str = Field(...)

    def hash_password(self) -> bytes:
        hashed_password = bcrypt.hashpw(
            self.password.encode('utf-8'), bcrypt.gensalt(12))
        return hashed_password

    def check_password(self, hashed_password: bytes) -> bool:
        result = bcrypt.checkpw(self.password.encode('utf-8'), hashed_password)
        return result

    @staticmethod
    def encode_auth_token(username: str, token_type: str) -> str:
        try:
            if token_type == 'refresh_token':
                payload = {
                    'exp': datetime.now(timezone.utc) + timedelta(days=0, minutes=30),
                    'token_type': token_type,
                    'sub': username
                }
            elif token_type == 'access_token':
                payload = {
                    'exp': datetime.now(timezone.utc) + timedelta(days=0, minutes=1),
                    'token_type': token_type,
                    'sub': username
                }
            return jwt.encode(
                payload,
                # app.config.get('SECRET_KEY'),
                "dev",
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(token: str) -> str:
        try:
            payload = jwt.decode(token, "dev", algorithms=['HS256'])
            return payload
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again.'
