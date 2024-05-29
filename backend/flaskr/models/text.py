from pydantic import BaseModel, Field


class Text(BaseModel):
    author: str = Field(...)
    content: str = Field(...)
