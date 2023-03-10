from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, Float, Date, Time, BigInteger, ForeignKey, TIMESTAMP, Text, LargeBinary, Boolean

TIME_SERIES_DATABASE = "postgresql://postgres:hoge@localhost:5432/time_series"

Engine = create_engine(TIME_SERIES_DATABASE)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

class TimeSeries_v1(Base):
    __tablename__ = 'time_series_v1'

    device_id = Column(String(50), primary_key=True)
    date_time = Column(TIMESTAMP, primary_key=True)
    sensor_value = Column(Float, nullable=False)

class TimeSeries_v2(Base):
    __tablename__ = 'time_series_v2'

    device_id = Column(String(50), primary_key=True)
    date_time = Column(TIMESTAMP, primary_key=True)
    sensor_value = Column(Float, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)

'''
CREATE TABLE time_series_v2_2023_03_12 (
    CONSTRAINT time_series_v2_2023_03_12_check CHECK (date_time >= DATE '2023-03-12' AND date_time < DATE '2023-03-13')
) INHERITS (time_series_v2);
'''