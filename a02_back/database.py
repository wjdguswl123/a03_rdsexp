
import pymysql
import os
from dotenv import load_dotenv

# 1. 현재 database1.py가 있는 폴더 확인
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 2. 같은 폴더에 있는 .env 불러오기
load_dotenv(os.path.join(BASE_DIR, ".env"), override=True)


# 3. 데이터베이스 접속 함수
def get_db_conn():

    conn = pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASS"),
        db=os.getenv("DB_NAME"),
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )

    return conn


# 4. 영웅 검색 함수
def select_heros(nickname, job_class):

    conn = get_db_conn()

    try:
        with conn.cursor() as cursor:

            sql = """
                SELECT *
                FROM heros
                WHERE nickname LIKE %s
                AND job_class LIKE %s
            """

            data = (
                f"%{nickname}%",
                f"%{job_class}%"
            )

            cursor.execute(sql, data)

            heros = cursor.fetchall()

        return heros

    finally:
        conn.close()
