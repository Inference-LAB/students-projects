from database import SessionLocal
from models import Student,Course,Enrollment





                       #function for students and crud

def create_student():
    

                               #CREATE SESSION FACTORY:
    session=SessionLocal()

    name=input("enter name: ")
    roll_number=(input("enter roll number: "))
    email=input("enter email:")
    department=input("enter department:")
    semester=int(input("enter semester:"))
    cgpa=float(input("enter cgpa: "))

    new_student=Student(

        name=name,
        roll_number=roll_number,
        email=email,
        department=department,
        semester=semester,
        cgpa=cgpa
    )

    session.add(new_student)

    session.commit()

    session.close()


def view_students():
   
   session=SessionLocal()

   all_students=session.query(Student).all()

   if not all_students:
        print("Students not found")

    
   else:
      
      for row in all_students:
          print("student name is:",row.name)
          print("student roll number is:",row.roll_number)
          print("email is:",row.email)
          print("department is:",row.department)
          print("semester is:",row.semester)
          print("cgpa is :",row.cgpa)
          print("done")
          
       
      session.close()


def update_student():


     session=SessionLocal()

     student_id=int(input("enter student id:"))

     student=session.query(Student).filter_by(student_id=student_id).first()

     if student:
         student.name=input("enter name:")
         student.roll_number=input("enter roll number:")
         student.email=input("enter email:")
         student.department=input("enter department name:")
         student.semester=int(input("enter semester:"))
         student.cgpa=float(input("enter cgpa:"))


     else:
         print("student not found.")

     session.commit()
     print("student updated successfully.")
     session.close()


def delete_student():

    session=SessionLocal()

    stu_id=int(input("enter student is to delete:"))

    student=session.query(Student).filter_by(student_id=stu_id).first()

    if student:
        session.delete(student)

        session.commit()
        print("student deleted successfully:")

    else:
        print("Stusent not found")

    session.close()



                       #defines table for course:

def create_course():

    session = SessionLocal()

    course_name = input("Enter course name:")
    course_code = input("Enter course code:")
    credit_hours = int(input("Enter credit hours:"))
  #below lines are just like Inserting in SQL:
    new_course = Course(

        course_name=course_name,
        course_code=course_code,
        credit_hours=credit_hours
    )

    session.add(new_course)

    session.commit()

    print("Course added successfully.")

    session.close()
                                      #second function of course table:
def view_courses():

    session = SessionLocal()

    all_courses = session.query(Course).all()
 #it means if no students found then:
    if not all_courses:
        print("Courses not found.")

    else:

        for row in all_courses:
            print("Course ID:", row.course_id)
            print("Course Name:", row.course_name)
            print("Course Code:", row.course_code)
            print("Credit Hours:", row.credit_hours)
            print()

    session.close()

def update_course():

    session = SessionLocal()

    course_id = int(input("Enter course id: "))

    course = session.query(Course).filter_by(course_id=course_id).first()

    if course:

        course.course_name = input("Enter course name:")
        course.course_code = input("Enter course code:")
        course.credit_hours = int(input("Enter credit hours:"))

        session.commit()

        print("Course updated successfully.")

    else:
        print("Course not found.")

    session.close()

def delete_course():

    session = SessionLocal()

    course_id = int(input("Enter course id to delete: "))

    course = session.query(Course).filter_by(course_id=course_id).first()

    if course:

        session.delete(course)

        session.commit()

        print("Course deleted successfully.")

    else:
        print("Course not found.")

    session.close()


def enroll_student():

    session = SessionLocal()

    student_id = int(input("Enter student id: "))
    course_id = int(input("Enter course id: "))
    grade = input("Enter grade: ")

    new_enrollment = Enrollment(

        student_id=student_id,
        course_id=course_id,
        grade=grade
    )

    session.add(new_enrollment)

    session.commit()

    print("Student enrolled successfully.")

    session.close()

#function which describe who is enrolling in course:
def view_enrollments():

    session = SessionLocal()

    all_enrollments = session.query(Enrollment).all()

    if not all_enrollments:
        print("Enrollments not found.")

    else:

        for row in all_enrollments:

            print("Enrollment ID:", row.id)
            print("Student ID:", row.student_id)
            print("Course ID:", row.course_id)
            print("Grade:", row.grade)
            print()

    session.close()


                              #update the enrollment table:
def update_enrollment():

    session = SessionLocal()

    enrollment_id = int(input("Enter enrollment id: "))
    enrollment = session.query(Enrollment).filter_by(id=enrollment_id).first()

    if enrollment:
        enrollment.student_id = int(input("Enter student id: "))
        enrollment.course_id = int(input("Enter course id: "))
        enrollment.grade = input("Enter grade: ")

        session.commit()

        print("Enrollment updated successfully.")

    else:
        print("Enrollment not found.")

    session.close()

def delete_enrollment():

    session = SessionLocal()

    enrollment_id = int(input("Enter enrollment id to delete: "))
    enrollment = session.query(Enrollment).filter_by(id=enrollment_id).first()

    if enrollment:

        session.delete(enrollment)
#it does the save chnages:
        session.commit()

        print("Enrollment deleted successfully.")

    else:
        print("Enrollment not found.")

    session.close()



           
    
        


       
   
    

