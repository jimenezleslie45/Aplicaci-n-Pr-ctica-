from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, field_validator
import re

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @field_validator('name')
    @classmethod
    def valid_name(cls, v: str):
        if not v or len(v.strip()) < 2:
            raise ValueError("El nombre debe tener al menos 2 caracteres.")
        if not v.replace(" ", "").isalpha():
            raise ValueError("El nombre solo puede contener letras.")
        return v.strip().title()

    @field_validator('age')
    @classmethod
    def valid_age(cls, v: int):
        if not 15 <= v <= 120:
            raise ValueError("La edad debe estar entre 15 y 120 años.")
        return v

# --- NUEVA RUTA AGREGADA PARA LA PÁGINA DE INICIO ---
@app.get("/")
def read_root():
    return {"message": "¡Hola! Mi servidor FastAPI está funcionando."}

# --- RUTA EXISTENTE PARA REGISTRO ---
@app.post("/register")
async def register(user: User):
    return {"message": "Registro exitoso", "user": user}