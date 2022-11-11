from pydantic import BaseModel, EmailStr
from typing import List

class Types(BaseModel):
    type: str


class Weaknesses(BaseModel):
    weakness: str


class User(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserLogin(BaseModel):
    username: str
    password: str


class Pokemon(BaseModel):
    id: int
    name: str
    category: str
    image_url: str
    types: List[Types]
    weaknesses: List[Weaknesses]
