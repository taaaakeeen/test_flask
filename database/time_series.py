from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, Float, Date, Time, BigInteger, ForeignKey, TIMESTAMP, Text, LargeBinary, Boolean

TIME_SERIES_DATABASE = "postgresql://postgres:hoge@localhost:5432/time_series"

Engine = create_engine(TIME_SERIES_DATABASE)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

class Data(Base):
    __tablename__ = 'data'

    id = Column(String(50), primary_key=True)
    date_time = Column(TIMESTAMP, primary_key=True)
    value = Column(Float, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)