from sqlalchemy import String, Integer, create_engine, Column, ForeignKey, Float
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///company_db.db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()

Base = declarative_base()

class Company(Base):

    __tablename__= "companies"

    id = Column(Integer, primary_key=True, autoincrement=True)

    products = relationship("Product", back_populates="company")

class Product(Base):

    __tablename__= "products"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    price = Column(Float, nullable=True)

    company_id = Column(Integer, ForeignKey("companies.id"))

    company = relationship("Company", back_populates="products")

Base.metadata.create_all(engine)

comp = Company()
db.add(comp)
db.commit()

product_01 = Product(name = "Phone", price = 15000, company_id = comp.id)

product_02 = Product(name = "Laptop", price = 85000, company_id = comp.id)


db.add_all([product_01, product_02])

print("all fine")

