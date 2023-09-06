# FastAPI Backend con MySQL

Microservicio rest-api desarrollado utilizando el framework de Python FastAPI con conexión a una base de datos MySQL. Nos permite obtener los autores a través de un ID e insertar los mismos a la BD.

## Requisitos previos
- Python3
- MySQL

## Configuración

### Entorno Virtual (Opcional)

Se recomienda utilizar un entorno virtual como lo es venv para este proyecto.
Si desea utilizarlo ejecutar los siguientes comandos:
```bash
python3 -m venv fastapi-venv
fastapi-venv\Scripts\activate.bat
```

### Instalación de Dependencias

Proporciono un archivo requirements.txt el cual brinda todos los requisitos necesarios para ejecutar el microservicio. Simplemente tienen que asegurarse de ejecutar el comando: 
```bash
pip install -r requirements.txt
```

### Base de datos

Asegurate de configurar la conexión a tu base de datos MySQl en el archivo /config/db.py

### Iniciar Aplicación

Una vez hecho todo, lo único que queda es ejecutar el siguiente comando:
```bash
uvicorn main:app --reload
```

##Autor
👨‍💻**[Lautaro Suárez]**(https://github.com/Lautisuarez)