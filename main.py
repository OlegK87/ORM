import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book

DSN = 'postgresql://postgres:Motocikl@localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

session.close()

