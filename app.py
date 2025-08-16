from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, EmailStr, validator

app = FastAPI()

class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @validator('name')
    def name_validator(cls, v):
        if len(v.strip()) < 2:
            raise ValueError("Minimo 2 caracteres")
        return v.title()

    @validator('age')
    def age_validator(cls, v):
        if v < 13 or v > 120:
            raise ValueError("Edad debe ser 13-120")
        return v

users_db = []

@app.post("/register/")
async def register(user: User):
    users_db.append(user)
    return {"message": "Registro exitoso", "user": user}

@app.get("/users/")
async def get_users():
    return {"users": users_db}