import psycopg2

def connection():
    con = psycopg2.connect(
        database="pokemon",  # DB_NAME
        user="postgres",  # USER_NAME
        password="123",  # PASSWORD
        host="127.0.0.1",  # example.com
        port="5432"  # PORT
    )
    return con