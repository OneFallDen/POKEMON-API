from connect import connection
from models import Pokemon, User, UserLogin


# Get pokemon by id
def get_by_id(id_pokemon: int, request: str):
    con = connection()
    cur = con.cursor()
    cur.execute(request)
    rows = cur.fetchall()
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
    con.close()
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url, 'types': types,
            'weaknesses': weaknesses}


# Get pokemon by name
def get_by_name(name: str, request: str):
    con = connection()
    cur = con.cursor()
    cur.execute(request)
    rows = cur.fetchall()
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
    con.close()
    return {'id': id_pokemon, 'name': name, 'category': category, 'image_url': image_url, 'types': types,
            'weaknesses': weaknesses}


# Add new pokemon [ Create new pokemon ]
def add_pokemon(pokemon: Pokemon):
    con = connection()
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO pokemon (id, name, category, image_url) VALUES({pokemon.id},'{pokemon.name}','{pokemon.category}','{pokemon.image_url}');")
    con.commit()
    for type in pokemon.types:
        cur.execute(f"INSERT INTO type (id_pokemon, type) VALUES ({pokemon.id},'{type.type}');")
        con.commit()
    for weakness in pokemon.weaknesses:
        cur.execute(f"INSERT INTO weaknesses (pokemon_id, weakness) VALUES ({pokemon.id},'{weakness.weakness}');")
        con.commit()
    con.close()
    return f"{pokemon.name} added successfully"


# Check user in already registered
def check_user_not_exist(user: User):
    con = connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{user.username}';")
    rows = cur.fetchall()
    if len(rows) == 0:
        return True
    return False


# Sign up user [ User registration ]
def sign_up_user(user: User):
    if check_user_not_exist(user):
        return create_user(user)
    return {"User already exist!"}


# Add new user in DB [ Create new user ]
def create_user(user: User):
    con = connection()
    cur = con.cursor()
    cur.execute(
        f"INSERT INTO users (username, email, password) VALUES('{user.username}','{user.email}','{user.password}');")
    con.commit()
    return {"User has been created!"}


# Validate user
def check_user(user: UserLogin):
    con = connection()
    cur = con.cursor()
    cur.execute(f"SELECT * FROM users WHERE username = '{user.username}' AND password = '{user.password}';")
    rows = cur.fetchall()
    if len(rows) == 1:
        return True
    return False
