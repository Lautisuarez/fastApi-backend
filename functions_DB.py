from sqlalchemy.orm import Session
from model.author import Author as AuthorModel
from schemas.class_author import Author

def get_author(db: Session, id: int):
    """  
        Devuelve un autor de la BD que tenga el mismo ID que el pasado por parametro
        Argumentos:
        db - es la sesion actual de la BD
        id - es el ID del author a buscar, debe ser un int
    """
    return db.query(AuthorModel).filter(AuthorModel.id == id).first()

def insert_author(db: Session, author: Author):
    """ 
        Inserta un autor a la BD y lo retorna
        Argumentos:
        db - es la sesion actual de la BD
        author - es el nuevo autor a agregar, debe ser de la clase Author  
    """
    db_author = AuthorModel(field_1=author.field_1, author=author.author, description=author.description, my_numeric_field=author.my_numeric_field)
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return db_author