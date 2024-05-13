from pydantic import BaseModel, Field
import uuid
from typing import Optional


class User(BaseModel):
    # id: str = Field(default_factory=uuid.uuid4, alias="_id")
    id: str = Field(...)
    username: str = Field(...)
    password: str = Field(...)
