import json
import sqlalchemy
from sqlalchemy.orm import sessionmaker

from models import create_tables, Publisher, Book, Shop, Stock, Sale

DSN = 'postgresql://postgres: @localhost:5432/netology_db'
engine = sqlalchemy.create_engine(DSN)

create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

with open('fixtures/tests_data.json', 'r') as fd:
    data = json.load(fd)

for record in data:
    model = {
        'publisher': Publisher,
        'shop': Shop,
        'book': Book,
        'stock': Stock,
        'sale': Sale,
    }[record.get('model')]
    session.add(model(id=record.get('pk'), **record.get('fields')))

session.commit()

name = input("Введите имя издателя: ")

for i in session.query(Publisher).filter(Publisher.name.like(f'%{name}%')).all():
    print(i)

number = input("Введите номер id издателя: ")

for j in session.query(Publisher).filter(Publisher.id == f'{number}').all():
    print(j)

session.close()

