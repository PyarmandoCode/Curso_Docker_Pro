#Instalando mi libreria o dependencia
from fastapi import FastAPI
#Creando la App
app=FastAPI()
@app.get("/")
def read_root():
    return {"message":"Servidor Web en Python"}


