from pydantic import BaseModel, Field
import uuid
from typing import Optional
import bcrypt


class User(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    id: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)

    def hash_password(self) -> str: 
        hashed_password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt(12))
        return hashed_password
    
    def check_password(self, hashed_password) -> bool:
        result = bcrypt.checkpw(self.password.encode('utf-8'), hashed_password)
        return result
