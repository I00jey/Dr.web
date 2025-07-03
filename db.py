import pymysql
import os
from dotenv import load_dotenv


# 환경 변수 로드
def load_config():
    load_dotenv(".env")


# DB 연결 함수
def get_db_connection():
    load_config()
    connect_db = pymysql.connect(
        user=os.getenv("DB_USER"),
        passwd=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        db=os.getenv("DB_NAME"),
        charset=os.getenv("DB_CHARSET"),
    )
    return connect_db


def get_cursor(conn):
    return conn.cursor()
