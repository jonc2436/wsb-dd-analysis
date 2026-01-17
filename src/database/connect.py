import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
PORT = os.getenv("PORT")

params = {
    'host': HOST,
    'dbname': DB_NAME,
    'user': POSTGRES_USERNAME,
    'password': POSTGRES_PASSWORD,
    'port': PORT
}

def connect_database():
    try:
        return psycopg2.connect(**params)
    except psycopg2.OperationalError as e:
        raise RuntimeError(f"Database connection failed: {e}")

def main():
    conn = connect_database()
    conn.close()

if __name__ == "__main__":
    main()