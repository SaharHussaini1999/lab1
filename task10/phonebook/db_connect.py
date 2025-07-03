import psycopg2
from config import load_config


def connect():
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        return conn
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
