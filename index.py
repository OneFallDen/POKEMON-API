from fastapi import FastAPI
import psycopg2

con = psycopg2.connect(
    database="DB_name",
    user="user",
    password="password",
    host="example.com",
    port="8000"
)

app = FastAPI()


@app.get('/')
def home():
    return 'Hello! It is Pokemon API'


@app.get('/id')
def get_pokemon_by_id(id_pokemon: int):
    return {'id': id_pokemon}
