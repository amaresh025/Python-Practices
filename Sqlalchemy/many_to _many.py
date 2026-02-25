from sqlalchemy import String, Integer, create_engine, ForeignKey, Column, Table
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

db_url = "sqlite:///courses_students_db.db"

engine = create_engine(db_url)

SessionLocal = sessionmaker(bind=engine)
db = SessionLocal()


Base = declarative_base()

Student_Course = Table(
    "student_course",
    Base.metadata,      
    Column("student_id", Integer, ForeignKey("student.id"), primary_key=True),
    Column("course_id", Integer, ForeignKey("course.id"), primary_key=True)
)

class Student(Base):
    __tablename__= "student"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    courses = relationship("Course", secondary=Student_Course, back_populates="students")



class Course(Base):

    __tablename__= "course"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    students = relationship("Student", secondary=Student_Course, back_populates="courses")

Base.metadata.create_all(engine)

s1 = Student(name = "Bob")
s2 = Student(name = "Alice")

c1 = Course(name = "Maths")
c2 = Course(name = "Physics")
c3 = Course(name = "Science")

s1.courses.append(c1)
s1.courses.append(c2)

s2.courses.append(c3)
s2.courses.append(c2)

db.add_all([s1, s2])

db.commit()

print("OKK...")
