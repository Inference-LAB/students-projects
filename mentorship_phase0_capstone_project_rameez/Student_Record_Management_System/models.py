from sqlalchemy import Column,String,Integer,Float,ForeignKey
from sqlalchemy.orm import declarative_base

Base=declarative_base()

class Student(Base):
    __tablename__="students"

    student_id = Column(Integer,primary_key=True)
    name =Column(String,nullable=False)
    roll_number=Column(String,nullable=False,unique=True)
    email=Column(String,nullable=False,unique=True)
    department=Column(String,nullable=False)
    semester=Column(Integer,nullable=False)
    cgpa=Column(Float)


class Course(Base):
    __tablename__="courses"


    course_id=Column(Integer,primary_key=True)
    course_name=Column(String,nullable=False)
    course_code=Column(String,nullable=False,unique=True)
    credit_hours=Column(Integer)


class Enrollment(Base):
    __tablename__="enrollments"

    id=Column(Integer,primary_key=True)
    student_id=Column(Integer,ForeignKey("students.student_id"))
    course_id=Column(Integer,ForeignKey("courses.course_id"))
    grade=Column(String)





#Mistakes made by me in that file:

#Unique=True U was capital which was wrong
#course_code datatype i used was Integer but suitable is String
#importing Foreign_key is wrong,correct is ForeignKey
#forgot to make foreignKey in enrollment table
    
