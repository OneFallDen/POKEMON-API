from fastapi import APIRouter, Depends
from auth.jwt_bearer import jwtBearer
from models.user_models import User, UserLogin, Favorite
from controllers.user_controller import signup_user, login_user, get_favorite, add_pokemon_in_favorite, \
    delete_pokemon_from_favs


router = APIRouter()


# User Sing up [ Create a new user ]
@router.post("/user/signup", tags=["user"])
def user_signup(user: User):
    return signup_user(user)


# User login
@router.post("/user/login", tags=["user"])
def user_login(user: UserLogin):
    return login_user(user)


# Get favorite user's pokemons by username
@router.get("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def get_favs(username: str):
    return get_favorite(username)


# Add pokemon to favorite
@router.post("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def add_favs(favs: Favorite):
    return add_pokemon_in_favorite(favs)


# Delete pokemon from favorite
@router.delete("/user/favorite", dependencies=[Depends(jwtBearer())], tags=["user"])
def delete_from_favs(favs: Favorite):
    return delete_pokemon_from_favs(favs)

