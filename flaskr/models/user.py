from pydantic import BaseModel, Field
import uuid
from typing import Optional


class User():
    id: str = Field(default_factory=uuid.uuid4, alias="_id")
    username: str = Field(...)
    password: str = Field(...)

