import psycopg2
import os
from dotenv import load_dotenv


# 환경 변수 로드
def load_config():
    load_dotenv(".env")


# DB 연결 함수
def get_db_connection():
    load_config()
    conn = psycopg2.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        dbname=os.getenv("DB_NAME"),
        port=os.getenv("DB_PORT"),
        options="-c client_encoding=UTF8",
    )
    return conn


def get_cursor(conn):
    return conn.cursor()
