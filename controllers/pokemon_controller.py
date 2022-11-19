from connect import connection
from models.pokemon_models import Pokemon
from fastapi import HTTPException

reqpok = "SELECT pokemon.id, pokemon.name,  pokemon.category, pokemon.image_url, type.type, weaknesses.weakness FROM " \
        "pokemon JOIN type ON pokemon.id = id_pokemon  JOIN weaknesses ON pokemon.id = pokemon_id  WHERE "


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


def get_pokemon_by_id(id_pokemon: int):
    req = reqpok + f"id = {id_pokemon};"
    return get_by_id(id_pokemon, req)


def get_pokemon_by_name(name: str):
    req = reqpok + f"name = '{name}';"
    return get_by_name(name, req)


# Add new pokemon [ Create new pokemon ]
def add_pokemon_bd(pokemon: Pokemon):
    post_req(
        f"INSERT INTO pokemon (id, name, category, image_url) VALUES({pokemon.id},'{pokemon.name}','{pokemon.category}'"
        f",'{pokemon.image_url}');")
    for type in pokemon.types:
        post_req(f"INSERT INTO type (id_pokemon, type) VALUES ({pokemon.id},'{type.type}');")
    for weakness in pokemon.weaknesses:
        post_req(f"INSERT INTO weaknesses (pokemon_id, weakness) VALUES ({pokemon.id},'{weakness.weakness}');")
    return HTTPException(status_code=201, detail='Pokemon added successfully!')


def get_by_id(id_pokemon: int, request: str):
    rows = get_req(request)
    weaknesses = []
    types = []
    for row in rows:
        name = row[1]
        category = row[2]
        image_url = row[3]
        if row[4] not in types:
            types.append(row[4])
        if row[5] not in weaknesses:
            weaknesses.append(row[5])
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url, 'types': types,
            'weaknesses': weaknesses}


# Get pokemon by name
def get_by_name(name: str, request: str):
    rows = get_req(request)
    weaknesses = []
    types = []
    for row in rows:
        id_pokemon = row[0]
        category = row[2]
        image_url = row[3]
        if row[4] not in types:
            types.append(row[4])
        if row[5] not in weaknesses:
            weaknesses.append(row[5])
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url, 'types': types,
            'weaknesses': weaknesses}
