import psycopg2

def connection():
    con = psycopg2.connect(
        database="DB_NAME",  # DB_NAME
        user="USER_NAME",  # USER_NAME
        password="PASSWORD",  # PASSWORD
        host="example.com",  # example.com
        port="PORT"  # PORT
    )
    return con