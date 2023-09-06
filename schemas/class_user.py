from pydantic import BaseModel, Field

class User(BaseModel):
    """  
        Clase Author
    """
    id: int = Field(default=None, ge=1)
    username: str
    password: str
    