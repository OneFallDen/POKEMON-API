from fastapi import FastAPI, Depends
from functions import get_by_id, get_by_name, add_pokemon, sign_up_user, check_user, get_user_id_by_name, \
    get_favorite_by_id, add_pokemon_in_favs, delete_pokemon_from_favs
from models import Pokemon, User, UserLogin, Favorite
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer

app = FastAPI()

reqpok = "SELECT pokemon.id, pokemon.name,  pokemon.category, pokemon.image_url, type.type, weaknesses.weakness FROM " \
        "pokemon JOIN type ON pokemon.id = id_pokemon  JOIN weaknesses ON pokemon.id = pokemon_id  WHERE "


# Home Page
@app.get('/', tags=["home"])
def home():
    return 'Hello! It is Pokemon API'


# Get pokemon by id
@app.get('/id', tags=["pokemon"])
def get_pokemon_by_id(id_pokemon: int):
    req = reqpok + f"id = {id_pokemon};"
    return get_by_id(id_pokemon, req)


# Get pokemon by name
@app.get('/name', tags=["pokemon"])
def get_pokemon_by_name(name: str):
    req = reqpok + f"name = '{name}';"
    return get_by_name(name, req)


# Add new pokemon [ Create a new pokemon ]
@app.post('/pokemon', dependencies=[Depends(jwtBearer())], tags=["pokemon"])
def add_pokemon(pokemon: Pokemon):
    return add_pokemon(pokemon)


# User Sing up [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup(user: User):
    sign_up_user(user)
    return signJWT(user.username)


# User login
@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin):
    if check_user(user):
        return signJWT(user.username)
    else:
        return {
            "error": "Invalid login or password!"
        }


# Get favorite user's pokemons by username
@app.get("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def get_favs(username: str):
    userID = get_user_id_by_name(username)
    pokemons = get_favorite_by_id(userID)
    pokemons_to_return = []
    for pokemon in pokemons:
        pokemons_to_return.append(get_pokemon_by_id(pokemon))
    return pokemons_to_return


# Add pokemon to favorite
@app.post("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def add_favs(favs: Favorite):
    return add_pokemon_in_favs(get_user_id_by_name(favs.username), favs.pokemonID)


# Delete pokemon from favorite
@app.delete("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def delete_from_favs(favs: Favorite):
    return delete_pokemon_from_favs(favs)
