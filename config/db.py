from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv() # Cargamos las variables de entorno
# y las asignamos
MYSQL_HOST= os.getenv("MYSQL_HOST")
MYSQL_PORT= os.getenv("MYSQL_PORT")
MYSQL_USER= os.getenv("MYSQL_USER")
MYSQL_PASSWORD= os.getenv("MYSQL_PASSWORD")
MYSQL_DB= os.getenv("MYSQL_DB")

SQLALCHEMY_DATABASE_URL = f"mysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}"
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
