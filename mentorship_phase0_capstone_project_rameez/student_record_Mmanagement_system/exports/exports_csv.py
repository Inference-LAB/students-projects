import csv
from database import SessionLocal
from models import Student
from models import Course
from models import Enrollment

def export_students_to_csv():

    session=SessionLocal()

    #that line fetch the data from the Student table
    students=session.query(Student).all()

    with open("students.csv","w",newline="") as file:
        writer=csv.writer(file)

                 #header
                 #that writerow write the header mean header column of the table
        writer.writerow([    #here writerow just write one row mean header
            "student_id",
            "name",
            "roll_number",
            "department",
            "email",
            "semester",
            "cgpa"
        ])

                 #fetch all students data.
        for student in students:
            writer.writerow([
                 
                 student.student_id,
                 student.name,
                 student.roll_number,
                 student.department,
                 student.email,
                 student.semester,
                 student.cgpa
                    ])
    print("table exported in csv succesfully:")
    session.close()


def export_courses_to_csv():

    session = SessionLocal()

                              #fetch all data from Course table
    courses = session.query(Course).all()

    with open("courses.csv", "w", newline="") as file:
        writer = csv.writer(file)

                               #header
        writer.writerow([
            "course_id",
            "course_name",
            "course_code",
            "credit_hours"
        ])

                            #write course data
        for course in courses:
            writer.writerow([
                course.course_id,
                course.course_name,
                course.course_code,
                course.credit_hours
            ])

    print("Courses exported to CSV successfully.")
    session.close()


def export_enrollments_to_csv():

    session = SessionLocal()

                          #fetch all data from Enrollment table
    enrollments = session.query(Enrollment).all()

    with open("enrollments.csv", "w", newline="") as file:
        writer = csv.writer(file)

                                     #header
        writer.writerow([
            "enrollment_id",
            "student_id",
            "course_id",
            "grade"
        ])

                              #write enrollment data
        for enrollment in enrollments:
            writer.writerow([
                enrollment.id,
                enrollment.student_id,
                enrollment.course_id,
                enrollment.grade
            ])

    print("Enrollments exported to CSV successfully.")
    session.close()
            
                    
        
                   
        