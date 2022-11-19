from fastapi import FastAPI
from routes import pokemon_router, user_router, views_router

app = FastAPI()

app.include_router(pokemon_router.router)
app.include_router(user_router.router)
app.include_router(views_router.router)
