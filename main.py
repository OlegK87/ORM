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
for i in session.query(Shop).join(Stock, Shop.id == Stock.id_shop).join(Book, Book.id == Stock.id_book)\
        .join(Publisher, Publisher.id == Book.id_publisher).\
        filter(Publisher.name.like(f"{name}")).all():
    print(f"Магазин {i} продает книги издателя {name}")

id = input("Введите номер id издателя: ")
for j in session.query(Shop).join(Stock, Shop.id == Stock.id_shop).join(Book, Book.id == Stock.id_book)\
        .join(Publisher, Publisher.id == Book.id_publisher).\
        filter(Publisher.id == f'{id}').all():
      print(f"Магазин {j} продает книги издателя {id}")

session.close()

