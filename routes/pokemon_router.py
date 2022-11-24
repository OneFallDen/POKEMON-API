from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from auth.jwt_bearer import jwtBearer
from models.pokemon_models import Pokemon
from controllers.pokemon_controller import get_pokemon_by_id, get_pokemon_by_name, add_pokemon_bd, pokemon_get

router = APIRouter()


# Get pokemon by id
@router.get('/id', tags=["pokemon"])
def get_pokemon_id(pokemon_id: int):
    return get_pokemon_by_id(pokemon_id)


# Get pokemon by name
@router.get('/name', tags=["pokemon"])
def get_pokemon_name(name: str):
    return JSONResponse(get_pokemon_by_name(name))


# Get pokemon by id or name
@router.get('/pokemon', tags=["pokemon"])
def get_pokemon(att):
    return pokemon_get(att)


# Add new pokemon [ Create a new pokemon ]
@router.post('/pokemon', dependencies=[Depends(jwtBearer())], tags=["pokemon"])
def add_pokemon(pokemon: Pokemon):
    return add_pokemon_bd(pokemon)
