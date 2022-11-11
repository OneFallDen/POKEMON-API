from fastapi import FastAPI
import functions
from models import Pokemon

app = FastAPI()

reque = "SELECT pokemon.id, pokemon.name,  pokemon.category, pokemon.image_url, type.type, weaknesses.weakness FROM " \
        "pokemon JOIN type ON pokemon.id = id_pokemon  JOIN weaknesses ON pokemon.id = pokemon_id  WHERE "


@app.get('/')
def home():
    return 'Hello! It is Pokemon API'


@app.get('/id')
def get_pokemon_by_id(id_pokemon: int):
    req = reque + f"id = {id_pokemon};"
    return functions.get_by_id(id_pokemon, req)


@app.get('/name')
def get_pokemon_by_name(name: str):
    req = reque + f"name = '{name}';"
    return functions.get_by_name(name, req)


@app.post('/pokemon')
def add_pokemon(pokemon: Pokemon):
    return functions.add_pokemon(pokemon)
