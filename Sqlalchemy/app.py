from sqlalchemy import create_engine, Column, String, Integer, Float
from sqlalchemy.orm import declarative_base, sessionmaker

db_url = "sqlite:///database.db"
engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()


Base = declarative_base()

class Product(Base):
    __tablename__= "product"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    price = Column(Float)
    quantity = Column(Integer)


Base.metadata.create_all(engine)

product = Product(
    name = "Phone",
    price = 22000,
    quantity = 50
)
product2 = db.query(Product).filter(Product.name == "Phone").first()
db.add(product)
db.commit()
db.close()
print("everything is OK")