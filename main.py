from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.responses import JSONResponse
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from typing import Annotated
from sqlalchemy.orm import Session
from schemas.class_author import Author as AuthorSchema
from functions_DB import *
from config.db import SessionLocal, engine, Base

app = FastAPI(title="FastAPI Backend", description="a REST-API using fastAPI and MySQL")
security = HTTPBasic()
Base.metadata.create_all(bind=engine)


def get_db():
    """ 
        Crea un generador de la sesion de la BD y la devuelve
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_security(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db: Session = Depends(get_db)):
    """  
        Verifica si el usuario esta autenticado
        Argumentos:
        credentials - son las credenciales que el usuario envia, tiene username y password
        db - es la sesion actual de la BD 
    """
    userDB = get_user(db, credentials.username)
    try:
        if (credentials.username == userDB.username and credentials.password == userDB.password):
            return True
    except:
        return False
    return False

@app.get("/data/{id}", response_model=AuthorSchema)
def get_data_id(isLogin: Annotated[str, Depends(get_security)], id: int, db: Session = Depends(get_db)):
    """ 
        Retorna al autor que se encuentra en la BD que tenga el mismo ID pasado por parametro, 
        en caso de que no exista se retorna un error 404.
        Argumentos:
        isLogin - True si el usuario esta autenticado, False caso contrario
        id - es el ID del author a buscar, debe ser un int
        db - es la sesion actual de la BD 
    """
    print(isLogin)
    if not(isLogin): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    db_author = get_author(db, id)
    if(db_author is None):
        raise HTTPException(status_code=404, detail="Author not found")
    return db_author

@app.post("/input/{my_target_field}", response_model=AuthorSchema)
def post_field(isLogin: Annotated[str, Depends(get_security)], my_target_field: str, author: Author, db: Session = Depends(get_db)):
    """ 
        Retorna un diccionario con el ID del autor que se agregó a la BD
        Argumentos:
        isLogin - True si el usuario esta autenticado, False caso contrario
        my_target_field - el campo a convertir a mayuscula, debe ser string
        author - es el nuevo autor a agregar, debe ser de la clase Author 
        db - es la sesion actual de la BD 
    """
    if not(isLogin): raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password")
    targets_field = ["author", "field_1", "description"]
    if(my_target_field in targets_field):
        setattr(author, my_target_field, getattr(author, my_target_field).upper())
        new_author = insert_author(db, author)
        return JSONResponse(content={"id": new_author.id})
    return JSONResponse(content={"error": f"{my_target_field} no es un campo válido para convertir a mayúscula"} )