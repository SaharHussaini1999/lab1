import psycopg2
from config import load_config


def connect():
    try:
        params = load_config()
        return psycopg2.connect(**params)
    except (Exception, psycopg2.DatabaseError) as error:
        print("Connection error:", error)
