
import pymysql
from app import app
import pandas as pd

def get_population_data():
    # 데이터베이스 연결
    conn = pymysql.connect(
        host=app.config['DB_HOST'],
        user=app.config['DB_USER'],
        password=app.config['DB_PASSWORD'],
        db=app.config['DB_NAME'],
        cursorclass=pymysql.cursors.DictCursor
    )

    try:
        with conn.cursor() as cursor:
            # 쿼리 실행
            cursor.execute("SELECT date, population, growth_rate FROM population_data ORDER BY date")
            result = cursor.fetchall()
            data = pd.DataFrame(result)

    finally:
        conn.close()

    return data
