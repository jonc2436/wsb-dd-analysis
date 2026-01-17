import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

HOST = os.getenv("HOST")
DB_NAME = os.getenv("DB_NAME")
POSTGRES_USERNAME = os.getenv("POSTGRES_USERNAME")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
PORT = os.getenv("PORT")

conn = psycopg2.connect(
    host=HOST,
    dbname=DB_NAME,
    user=POSTGRES_USERNAME,
    password=POSTGRES_PASSWORD,
    port=PORT
)

cur = conn.cursor()

