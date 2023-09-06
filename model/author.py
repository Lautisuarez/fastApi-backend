from sqlalchemy import Column, Integer, String
from config.db import Base

class Author(Base):
    """  
        Modelo para la tabla en la BD
    """
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, autoincrement=True)
    field_1 = Column(String(50))
    author = Column(String(50))
    description = Column(String(200))
    my_numeric_field = Column(Integer)