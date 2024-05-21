from pydantic import BaseModel, Field

class Text(BaseModel):
    textId: str = Field(...)
    authorId: str = Field(...)
    content: str = Field(...)