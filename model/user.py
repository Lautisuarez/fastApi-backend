from sqlalchemy import Column, Integer, String
from config.db import Base

class User(Base):
    """  
        Modelo para la tabla en la BD
    """
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(255))
    password = Column(String(255))