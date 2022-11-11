from pydantic import BaseModel
from typing import List

class Types(BaseModel):
    type: str


class Weaknesses(BaseModel):
    weakness: str


class User(BaseModel):
    id: int
    username: str
    password: str


class Pokemon(BaseModel):
    id: int
    name: str
    category: str
    image_url: str
    types: List[Types]
    weaknesses: List[Weaknesses]
