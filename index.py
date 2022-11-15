from fastapi import FastAPI
from routes import pokemon_router, user_router

app = FastAPI()

app.include_router(pokemon_router.router)
app.include_router(user_router.router)


# Home Page
@app.get('/', tags=["home"])
def home():
    return 'Hello! It is Pokemon API'
