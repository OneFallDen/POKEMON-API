from fastapi import FastAPI
import psycopg2
from connect import connection

app = FastAPI()


@app.get('/')
def home():
    return 'Hello! It is Pokemon API'


@app.get('/id')
def get_pokemon_by_id(id_pokemon: int):
    con = connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM pokemon WHERE id = {id_pokemon}")
    rows = cur.fetchall()
    for row in rows:
        name = row[1]
        category = row[2]
        image_url = row[3]
    con.close()
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url}


@app.get('/name')
def get_pokemon_by_name(name: str):
    con = connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM pokemon WHERE name = '{name}'")
    rows = cur.fetchall()
    for row in rows:
        id_pokemon = row[0]
        category = row[2]
        image_url = row[3]
    con.close()
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url}