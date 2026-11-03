
import pymysql
import os
from dotenv import load_dotenv


# 1. 현재 db_test.py 파일이 있는 폴더 확인
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# 2. 같은 폴더에 있는 .env 파일 불러오기
env_path = os.path.join(BASE_DIR, ".env")
load_dotenv(env_path, override=True)


# 3. 환경변수 확인
print(".env 파일 존재:", os.path.exists(env_path))
print("DB_HOST:", repr(os.getenv("DB_HOST")))
print("DB_NAME:", repr(os.getenv("DB_NAME")))


# 4. AWS RDS 데이터베이스 접속
conn = pymysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    db=os.getenv("DB_NAME"),
    charset="utf8mb4",
    cursorclass=pymysql.cursors.DictCursor
)

print("AWS RDS 접속 성공!")


# 5. 직원 데이터 조회
with conn.cursor() as cursor:

    sql = """
        SELECT empno, ename, job, sal
        FROM emp_test
        ORDER BY empno
    """

    cursor.execute(sql)

    emps = cursor.fetchall()


# 6. 조회된 직원 데이터 출력
print("\n===== 직원 목록 =====")

for emp in emps:
    print(emp)


# 7. 데이터베이스 접속 종료
conn.close()

print("\n데이터베이스 접속 종료!")
