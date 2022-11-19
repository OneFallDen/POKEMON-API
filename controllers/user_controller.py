from connect import connection
from models.user_models import User, UserLogin, Favorite
from fastapi import HTTPException
from auth.jwt_handler import signJWT
from .pokemon_controller import get_pokemon_by_id


# Form for get requests
def get_req(req):
    con = connection()
    cur = con.cursor()
    cur.execute(req)
    rows = cur.fetchall()
    con.close()
    return rows


# Form for post, delete, put requests
def post_req(req):
    con = connection()
    cur = con.cursor()
    cur.execute(req)
    con.commit()
    con.close()
    return HTTPException(status_code=200, detail="OK")


def signup_user(user: User):
    sign_up_user(user)
    return signJWT(user.username)


def login_user(user: UserLogin):
    if check_user(user):
        return signJWT(user.username)
    else:
        return {
            "error": "Invalid login or password!"
        }


def get_favorite(username: str):
    userID = get_user_id_by_name(username)
    pokemons = get_favorite_by_id(userID)
    pokemons_to_return = []
    for pokemon in pokemons:
        pokemons_to_return.append(get_pokemon_by_id(pokemon))
    return pokemons_to_return


# Method for router to add in favorite
def add_pokemon_in_favorite(favs: Favorite):
    return add_pokemon_in_favs(get_user_id_by_name(favs.username), favs.pokemonID)


# Delete pokemon from favorite
def delete_pokemon_from_favs(favs: Favorite):
    userID = get_user_id_by_name(favs.username)
    post_req(f"DELETE FROM favorite WHERE userid = {userID} AND pokemonid = {favs.pokemonID};")
    return HTTPException(status_code=200, detail="Successfully deleted from favorite!")


def add_pokemon_in_favs(userID: int, pokemonID: int):
    post_req(f"INSERT INTO favorite (userid, pokemonid) VALUES({userID}, {pokemonID});")
    return HTTPException(status_code=200, detail="Successfully added in favorite!")


# Get user id by username
def get_user_id_by_name(username: str):
    rows = get_req(f"SELECT * FROM users WHERE username = '{username}';")
    for row in rows:
        id_to_return = row[0]
    return id_to_return


# Get favorite pokemons by user id
def get_favorite_by_id(userID: int):
    rows = get_req(f"SELECT pokemonid FROM favorite WHERE userid = {userID};")
    pokemon_ids = []
    for row in rows:
        pokemon_ids.append(row[0])
    return pokemon_ids


# Validate user
def check_user(user: UserLogin):
    rows = get_req(f"SELECT * FROM users WHERE username = '{user.username}' AND password = '{user.password}';")
    if len(rows) == 1:
        return True
    return False


# Sign up user [ User registration ]
def sign_up_user(user: User):
    if check_user_not_exist(user):
        return create_user(user)
    return {"User already exist!"}


# Check user in already registered
def check_user_not_exist(user: User):
    rows = get_req(f"SELECT * FROM users WHERE username = '{user.username}';")
    if len(rows) == 0:
        return True
    return False


# Add new user in DB [ Create new user ]
def create_user(user: User):
    post_req(f"INSERT INTO users (username, email, password) VALUES('{user.username}','{user.email}','{user.password}')"
             f";")
    return HTTPException(status_code=201, detail='User created successfully!')
