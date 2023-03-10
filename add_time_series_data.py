from database.time_series import Session, Engine, TimeSeries_v1, TimeSeries_v2
import random
from datetime import datetime, timedelta
from sqlalchemy import text
from sqlalchemy import desc
import time

#####################################################################################

# 1h = 3600
# 1d = 86400
# 1w = 604800
# 1m = 2592000

MAX_ITERATIONS = 2592000
NOW_DATE_TIME = datetime.now()

def add_all_data(items):
    session = Session()
    session.add_all(items)
    session.commit()
    session.close()

def write_time_series_v1(device_id):
    items = []
    for i in range(MAX_ITERATIONS):
        date_time = NOW_DATE_TIME + timedelta(seconds=i)
        sensor_value = random.random()
        items.append(TimeSeries_v1(device_id=device_id, date_time=date_time, sensor_value=sensor_value))
    print(device_id, len(items))
    add_all_data(items)

def write_time_series_v2(device_id):
    items = []
    for i in range(MAX_ITERATIONS):
        date_time = NOW_DATE_TIME + timedelta(seconds=i)
        sensor_value = random.random()
        items.append(TimeSeries_v2(device_id=device_id, date_time=date_time, sensor_value=sensor_value))
    print(device_id, len(items))
    add_all_data(items)

device_list = [
    "camera_0",
    "camera_1",
    "camera_2",
    "camera_3",
    "camera_4",
    "camera_5",
    "camera_6",
    "camera_7",
    "camera_8",
    "camera_9",
]

def add_test_data_time_series_v1():
    for device_id in device_list:
        start_time = time.time()
        write_time_series_v1(device_id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"処理時間: {elapsed_time}秒")

def add_test_data_time_series_v2():
    for device_id in device_list:
        start_time = time.time()
        write_time_series_v2(device_id)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"処理時間: {elapsed_time}秒")

# 各デバイスの１か月データをtime_series_v1テーブルに書込む
# add_test_data_time_series_v1()

#####################################################################################

TODAY = "2023-03-10"

# SQL実行
def execute_sql(sql_text):
    conn = Engine.connect()
    result = conn.execute(text(sql_text))
    result.close()
    conn.close()

# 1日分のパーテションテーブル作成
def a_day_partition_table_sql(a_day):
    date = datetime.strptime(a_day, '%Y-%m-%d')
    next_day = date + timedelta(days=1)
    next_day_str = datetime.strftime(next_day, '%Y-%m-%d')
    sql_text = f'''
        CREATE TABLE time_series_v2_{a_day.replace("-","_")} (
            CONSTRAINT time_series_v2_{a_day.replace("-","_")}_check CHECK (date_time >= DATE '{a_day}' AND date_time < DATE '{next_day_str}')
        ) INHERITS (time_series_v2);
    '''
    return sql_text

# 60日分のパーテションテーブル作成
def create_partition_table():
    for i in range(60):
        today = datetime.strptime(TODAY, '%Y-%m-%d')
        today = today + timedelta(days=i)
        today_str = datetime.strftime(today, '%Y-%m-%d')
        print(today_str)

        sql_text = a_day_partition_table_sql(today_str)
        execute_sql(sql_text)

# time_series_v2テーブルにパーテション作成
# create_partition_table()

# 各デバイスの１か月データをtime_series_v2テーブルに書込む
# add_test_data_time_series_v2()

#####################################################################################

def add_test_data(device_id, date_time, sensor_value):
    print(device_id, date_time, sensor_value)
    session = Session()

    row = TimeSeries_v1(device_id=device_id, date_time=date_time, sensor_value=sensor_value)
    session.add(row)

    row = TimeSeries_v2(device_id=device_id, date_time=date_time, sensor_value=sensor_value)
    session.add(row)

    session.commit()
    session.close()

def append_test_rows():
    for i in range(25920000):
        date_time = NOW_DATE_TIME + timedelta(seconds=i)
        sensor_value = random.random()
        add_test_data("test", date_time, sensor_value)

# append_test_rows()
#####################################################################################

def get_rows_len():
    session = Session()
    record_count = session.query(TimeSeries_v1).count()
    print("v1", record_count)
    record_count = session.query(TimeSeries_v2).count()
    print("v2", record_count)

# get_rows_len()

#####################################################################################

def get_max_date_time_row(device_id, version):
    print(version)
    session = Session()
    if version == "v1":
        row = session.query(TimeSeries_v1).filter(TimeSeries_v1.device_id == device_id).order_by(desc(TimeSeries_v1.date_time)).first()
    else:
        row = session.query(TimeSeries_v2).filter(TimeSeries_v2.device_id == device_id).order_by(desc(TimeSeries_v2.date_time)).first()
    session.close()
    return row

def max_date_time_row():
    start_time = time.time()
    row = get_max_date_time_row("camera_4", "v1")
    print(row.device_id, row.date_time, row.sensor_value)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

    start_time = time.time()
    row = get_max_date_time_row("camera_4", "v2")
    print(row.device_id, row.date_time, row.sensor_value)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

    start_time = time.time()
    row = get_max_date_time_row("camera_4", "v1")
    print(row.device_id, row.date_time, row.sensor_value)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

    start_time = time.time()
    row = get_max_date_time_row("camera_4", "v2")
    print(row.device_id, row.date_time, row.sensor_value)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

max_date_time_row()
#####################################################################################

def get_a_day_rows(device_id, start, end, version):
    print(version)
    session = Session()
    if version == "v1":
        rows = session.query(TimeSeries_v1).filter(TimeSeries_v1.device_id == device_id).filter(TimeSeries_v1.date_time >= start, TimeSeries_v1.date_time < end).all()
    else:
        rows = session.query(TimeSeries_v2).filter(TimeSeries_v2.device_id == device_id).filter(TimeSeries_v2.date_time >= start, TimeSeries_v2.date_time < end).all()
    session.close()
    return rows

def select():
    start_time = time.time()
    rows = get_a_day_rows("camera_4", "2023-03-10", "2023-03-12", "v1")
    print(len(rows))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

    start_time = time.time()
    rows = get_a_day_rows("camera_4", "2023-03-10", "2023-03-12", "v2")
    print(len(rows))
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"処理時間: {elapsed_time}秒")

# select()

