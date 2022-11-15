from fastapi import APIRouter, Depends
from auth.jwt_bearer import jwtBearer
from models.pokemon_models import Pokemon
from controllers.pokemon_controller import get_pokemon_by_id, get_pokemon_by_name, add_pokemon_bd

router = APIRouter()


# Get pokemon by id
@router.get('/id', tags=["pokemon"])
def get_pokemon_id(pokemon_id: int):
    return get_pokemon_by_id(pokemon_id)


# Get pokemon by name
@router.get('/name', tags=["pokemon"])
def get_pokemon_name(name: str):
    return get_pokemon_by_name(name)


# Add new pokemon [ Create a new pokemon ]
@router.post('/pokemon', dependencies=[Depends(jwtBearer())], tags=["pokemon"])
def add_pokemon(pokemon: Pokemon):
    return add_pokemon_bd(pokemon)
