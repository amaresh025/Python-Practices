from sqlalchemy import String, Integer, Float, create_engine, ForeignKey, Column
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///empo_db.db"

engine = create_engine(db_url)

Session = sessionmaker(bind=engine)
db = Session()

Base = declarative_base()

class Employee(Base):
    __tablename__= "employees"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    department = Column(String, nullable=False)
    salary = Column(Float, nullable=False)

    emp_info = relationship("EmployeeInfo", back_populates="employee", uselist=False)

class EmployeeInfo(Base):
    __tablename__= "employee_info"

    employee_id = Column(Integer, ForeignKey("employees.id"), primary_key=True)
    phone = Column(Integer, nullable=False)
    address = Column(String, nullable=False)
    email = Column(String, nullable=False)

    employee = relationship("Employee", back_populates="emp_info")

Base.metadata.create_all(engine)

emp = Employee(name = "Yash Shukla", department = "IT", salary = 70000)
db.add(emp)
db.commit()
empinfo = EmployeeInfo(employee_id = emp.id, phone = 7775554422, address = "ballia", email = "yashshu@gamil.com")

db.add(empinfo)
db.commit()
db.close()

print("Everything is OKK")

