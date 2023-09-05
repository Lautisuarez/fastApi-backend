from fastapi import FastAPI, HTTPException
from model.class_author import Author

app = FastAPI()

authors = []

def get_new_id():
    """ 
    Retorna un int el cual es un nuevo ID  
    """
    return (authors[-1]["id"] + 1) if len(authors) > 0 else 1

def add_new_author(author: Author):
    """ 
    Agrega al autor pasado por parámetro a la BD
    Retorna un diccionario con el ID del nuevo actor agregado
    Argumentos:
    author - es el nuevo autor a agregar, debe ser de la clase Author 
    """
    author.id = get_new_id()
    authors.append(dict(author))
    return {"id": author.id}

@app.get("/data/{id}")
def get_data_id(id: int):
    """ 
        Retorna al autor con el mismo ID pasado por parametro, en caso de que no exista
        se retorna un error 404.
        Argumentos:
        id - es el ID del author a buscar, debe ser un int
    """
    for author in authors:
        if (author["id"] == id):
            return author
    raise HTTPException(status_code=404, detail="Author not found")

@app.post("/input/{my_target_field}")
def post_field(my_target_field: str, author: Author):
    """ 
        Retorna un diccionario con el ID del autor a agregar
        Argumentos:
        my_target_field - el campo a convertir a mayuscula, debe ser string
        author - es el nuevo autor a agregar, debe ser de la clase Author 
    """
    targets_field = ["author", "field_1", "description", "my_numeric_field"]
    if(my_target_field in targets_field):
        if(my_target_field == "my_numeric_field"):
            return {"error": "my_numeric_field no es un campo válido para convertir a mayúscula"}
        setattr(author, my_target_field, getattr(author, my_target_field).upper())
        return add_new_author(author)
    else:
        return {"error": f"{my_target_field} no es un campo válido para convertir a mayúscula"}