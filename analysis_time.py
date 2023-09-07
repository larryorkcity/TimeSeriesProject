
from .database import get_population_data
import numpy as np
import pandas as pd

from statsmodels.tsa.holtwinters import ExponentialSmoothing

# Exponential Smoothing을 사용하여 누락된 값을 예측
def exponential_smoothing_forecast(series):
    """
    Predict uncaught data by 'Exponential Smoothing'.

    Args: (pandas.Series)

    Returns: float (prediction)

    Example:
        forecasted_value = exponential_smoothing_forecast(df['Value'])
    """
    model = ExponentialSmoothing(series, trend='add', seasonal='add', seasonal_periods=7)
    model_fit = model.fit()
    forecast = model_fit.forecast(1)
    return forecast[0]


def print_values():
# 누락 값의 위치를 찾고나서 예측값으로 대체
    for i, row in df.iterrows():
        if pd.isnull(row['Value']):
            # 누락 값 예측
            forecasted_value = exponential_smoothing_forecast(df['Value'][:i])
            df.at[i, 'Value'] = forecasted_value

# 결과 출력
    print(df)
    return 0


def analyze_population_data():
    # 데이터베이스에서 인구수 데이터 가져오기
    data = get_population_data()

    # 데이터 분석 및 대시보드 생성 로직을 추가합니다.
    avg_population = data['population'].mean()
    min_population = data['population'].min()
    max_population = data['population'].max()
    
    # Calculate moving average and standard deviation
    data['moving_avg'] = data['population'].rolling(window=5).mean()
    data['std_dev'] = data['population'].rolling(window=5).std()
    
    # Calculate population growth rate (assuming data is sorted by date)
    data['growth_rate'] = data['population'].pct_change().fillna(0) * 100

    dashboard_data = {
        'average_population': avg_population,
        'min_population': min_population,
        'max_population': max_population,
        'data': data.to_dict(orient='records')
    }

    return dashboard_data




import time
import pymysql

class Node:
    def __init__(self, time, value):
        self.time = time
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, time, value):
        new_node = Node(time, value)
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next is not None:
                temp = temp.next
            temp.next = new_node

def measure_execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"실행 시간: {end_time - start_time} 초")
        return result
    return wrapper

def perform_database_operations():
    conn = pymysql.connect(
        host='host',
        user='user',
        password='test',
        db='TEST_DB',
        cursorclass=pymysql.cursors.DictCursor,
        isolation_level=pymysql.constants.ISOLATION_LEVEL_READ_COMMITTED
    )

    try:
        with conn.cursor() as cursor:
            cursor.execute("query1")
            result1 = cursor.fetchall()

            cursor.execute("query2")
            result2 = cursor.fetchall()

        conn.commit()

    except Exception as e:
        conn.rollback()
        print(f'에러 발생: {e}')

    finally:
        conn.close()

    return result1, result2

conn = pymysql.connect(
    host='host',
    user='user',
    password='test',
    db='TEST_DB',
    cursorclass=pymysql.cursors.DictCursor,
    isolation_level=pymysql.constants.ISOLATION_LEVEL_READ_COMMITTED
)

queries = []


def execute_queries(conn, queries):
    try:
        with conn.cursor() as cursor:
            results = []

            for query in queries:  # multiple queries from list
                cursor.execute(query)
                results.append(cursor.fetchall())

            delayed_commit(conn)  # Commit at regular intervals

        return results

    except Exception as e:
        conn.rollback()
        print(f'$$$ Err: {e}')
        return None
    
results = execute_queries(conn, queries)

if results is not None:
    for idx, result in enumerate(results):
        print(f"Result for Query {idx + 1}: {result}")

# Function for delayed commit
def delayed_commit(conn):
    try:
        conn.commit()
        print("Commit success!")
    except Exception as e:
        conn.rollback()
        print(f'Commit failed: {e}')

def repair_data_gaps(data):
    current_node = data.head
    while current_node.next is not None:
        time_diff = current_node.next.time - current_node.time
        if time_diff > 1:  # 1 시간 이상의 갭이 발견되면 데이터 복구 수행
            estimated_value = (current_node.value + current_node.next.value) / 2
            new_time = current_node.time + 1
            new_node = Node(new_time, estimated_value)
            new_node.next = current_node.next
            current_node.next = new_node
        current_node = current_node.next

@measure_execution_time
def main():
    result1, result2 = perform_database_operations()
    data = LinkedList()
    # 데이터 삽입 작업 (예: data.insert(time, value))
    repair_data_gaps(data)
    # 복구된 데이터 활용 등 추가 작업
