from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ARRAY, Float, Date, Time, BigInteger, ForeignKey, TIMESTAMP, Text, LargeBinary, Boolean
from sqlalchemy.dialects.postgresql import JSONB
from dotenv import load_dotenv
import os

load_dotenv()
KEIBA_DB =  os.environ['KEIBA_DB']

Engine = create_engine(KEIBA_DB)
Session = sessionmaker(bind=Engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    user_id = Column(String(50), primary_key=True)
    user_name = Column(String(50), unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)

    def __init__(self, user_id, user_name, password, email):
        self.user_id = user_id
        self.user_name = user_name
        self.password = password
        self.email = email
    
# class Poles(Base):
#     __tablename__ = "poles"
#     id = Column("id", Integer, primary_key=True)
#     ip = Column("ip", String, nullable=False)
#     name = Column("name", String, nullable=False)
#     gps = Column("gps", ARRAY(Float), nullable=False)
#     destination_ip = Column("destination_ip", String)
#     destination_port_used_for_udp = Column("destination_port_used_for_udp", Integer)
#     destination_port_used_for_tcp = Column("destination_port_used_for_tcp", Integer)

# class Daily(Base):
#     __tablename__ = "daily"
#     pole_id = Column("pole_id", Integer, ForeignKey('poles.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
#     date = Column("date", Date, primary_key=True)
#     traffic_volume = Column("traffic_volume", JSONB)

# class Detections(Base):
#     __tablename__ = "detections"
#     pole_id = Column("pole_id", Integer, ForeignKey('poles.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
#     date_time = Column("date_time", TIMESTAMP, primary_key=True)
#     detection = Column("detection", JSONB)

# class Images(Base):
#     __tablename__ = "images"
#     pole_id = Column("pole_id", Integer, ForeignKey('poles.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
#     date_time = Column("date_time", TIMESTAMP, primary_key=True)
#     image = Column("image", LargeBinary)
#     label = Column("label", Text)

# class Datasets(Base):
#     __tablename__ = "datasets"
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     created = Column("created", TIMESTAMP, nullable=False)
#     name = Column("name", String, unique=True, nullable=False)
#     classes = Column("classes", ARRAY(String), nullable=False)
#     type = Column("type", String, nullable=False)
#     merges = Column("merges", ARRAY(String))

# class DatasetFiles(Base):
#     __tablename__ = "dataset_files"
#     dataset_id = Column("dataset_id", Integer, ForeignKey('datasets.id', onupdate='CASCADE', ondelete='CASCADE'), primary_key=True)
#     file_name = Column("file_name", String, primary_key=True, nullable=False)
#     image = Column("image", LargeBinary, nullable=False)
#     label = Column("label", Text, nullable=False)
#     type = Column("type", String, nullable=False, primary_key=True)

# class Models(Base):
#     __tablename__ = "models"
#     id = Column("id", Integer, primary_key=True, autoincrement=True)
#     created = Column("created", TIMESTAMP, nullable=False)
#     dataset_id = Column("dataset_id", Integer, nullable=False)
#     dataset_name = Column("dataset_name", String, nullable=False)
#     project_name = Column("project_name", String, unique=True, nullable=False)
#     classes = Column("classes", ARRAY(String), nullable=False)
#     epochs = Column("epochs", Integer, nullable=False)
#     generate_succeed = Column("generate_succeed", Boolean, nullable=False)
#     generate_completed = Column("generate_completed", Boolean, nullable=False)

if __name__ == '__main__':
    Base.metadata.create_all(bind=Engine)