from fastapi import FastAPI
import psycopg2

con = psycopg2.connect(
    database="DB_NAME",  # DB_NAME
    user="USER_NAME",  # USER_NAME
    password="PASSWORD",  # PASSWORD
    host="example.com",  # example.com
    port="PORT"  # PORT
)

app = FastAPI()


@app.get('/')
def home():
    return 'Hello! It is Pokemon API'


@app.get('/id')
def get_pokemon_by_id(id_pokemon: int):
    cur = con.cursor()
    cur.execute(f"SELECT * FROM pokemon WHERE id = {id_pokemon}")
    rows = cur.fetchall()
    for row in rows:
        name = row[1]
        category = row[2]
        image_url = row[3]
    con.close()
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url}
