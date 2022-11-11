from fastapi import FastAPI, Depends
import functions
from models import Pokemon, User, UserLogin
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
    return functions.get_by_id(id_pokemon, req)


# Get pokemon by name
@app.get('/name', tags=["pokemon"])
def get_pokemon_by_name(name: str):
    req = reqpok + f"name = '{name}';"
    return functions.get_by_name(name, req)


# Add new pokemon [ Create a new pokemon ]
@app.post('/pokemon', dependencies=[Depends(jwtBearer())], tags=["pokemon"])
def add_pokemon(pokemon: Pokemon):
    return functions.add_pokemon(pokemon)


# User Sing up [ Create a new user ]
@app.post("/user/signup", tags=["user"])
def user_signup(user: User):
    functions.sign_up_user(user)
    return signJWT(user.username)


# User login
@app.post("/user/login", tags=["user"])
def user_login(user: UserLogin):
    if functions.check_user(user):
        return signJWT(user.username)
    else:
        return {
            "error": "Invalid login or password!"
        }
