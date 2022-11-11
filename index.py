from fastapi import FastAPI, Depends
import functions
from models import Pokemon, User, UserLogin
from auth.jwt_handler import signJWT
from auth.jwt_bearer import jwtBearer

app = FastAPI()

reque = "SELECT pokemon.id, pokemon.name,  pokemon.category, pokemon.image_url, type.type, weaknesses.weakness FROM " \
        "pokemon JOIN type ON pokemon.id = id_pokemon  JOIN weaknesses ON pokemon.id = pokemon_id  WHERE "


# Home Page
@app.get('/', tags=["home"])
def home():
    return 'Hello! It is Pokemon API'


# Get pokemon by id
@app.get('/id', tags=["pokemon"])
def get_pokemon_by_id(id_pokemon: int):
    req = reque + f"id = {id_pokemon};"
    return functions.get_by_id(id_pokemon, req)


# Get pokemon by name
@app.get('/name', tags=["pokemon"])
def get_pokemon_by_name(name: str):
    req = reque + f"name = '{name}';"
    return functions.get_by_name(name, req)


# Add new pokemon [ Create a new pokemon ]
@app.post('/pokemon', dependencies=[Depends(jwtBearer())], tags=["pokemon"])
def add_pokemon(pokemon: Pokemon):
    return functions.add_pokemon(pokemon)


# User Singup [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup(user: User):
    # add user
    return signJWT(user.username)


# Validate user login
def check_user(data: UserLogin):
    x = []
    for user in x:
        if user.username == data.username and user.password == data.password:
            return True
        return False


# User login
@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin):
    if check_user(user):
        return signJWT(user.username)
    else:
        return {
            "error": "Invalid login or password!"
        }
