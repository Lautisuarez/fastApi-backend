from pydantic import BaseModel, Field
from typing import Text

class Author(BaseModel):
    id: int = Field(default=None, ge=1)
    field_1: str
    author: str
    description: Text
    my_numeric_field: int
    