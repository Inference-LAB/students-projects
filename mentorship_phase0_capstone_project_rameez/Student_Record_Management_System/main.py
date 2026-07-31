
          #first we will import all the functions used in crud:
          #bcuz all function will be called here:
from crud import (
    create_student,
    view_students,
    update_student,
    delete_student,
    create_course,
    view_courses,
    update_course,
    delete_course,
    enroll_student,
    view_enrollments,
    update_enrollment,
    delete_enrollment

)


def menu():
                       #student functions
    print("1. Create Student")
    print("2. View Students")
    print("3. Update Student")
    print("4. Delete Student")
                       #course functions
    print("5. Create Course")
    print("6. View Courses")
    print("7. Update Course")
    print("8. Delete Course")
                       #enrollment functions
    print("9. Enroll Student")
    print("10. View Enrollments")
    print("11. Update Enrollment")
    print("12. Delete Enrollment")

    print("0. Exit")

               #creating separate function before the while true for storing statement is better approach


while True:

    menu()        # calling menu function to display all text

    choice = input("Enter your choice: ")

    if choice == "1":
        create_student()

    elif choice == "2":
        view_students()

    elif choice == "3":
        update_student()

    elif choice == "4":
        delete_student()

    elif choice == "5":
        create_course()

    elif choice == "6":
        view_courses()

    elif choice == "7":
        update_course()

    elif choice == "8":
        delete_course()

    elif choice == "9":
        enroll_student()

    elif choice == "10":
        view_enrollments()

    elif choice == "11":
        update_enrollment()

    elif choice == "12":
        delete_enrollment()

    elif choice == "0":
        print("Thank you for using Student Record Management System.")

                                   #while loop ends here
        break

    else:
        print("Invalid choice. Please try again.")