from database import (
    create_database,
    add_student,
    display_students,
    search_student
)

import pandas as pd
import numpy as np


def calculate_result(python_marks,database_marks,data_analysis_marks):
    total_marks=python_marks+database_marks+data_analysis_marks

    average=total_marks/3

    if average>=90:
        return "A+"
    elif average>=80:
        return "A"
    elif average>=70:
        return "B"
    elif average>=60:
        return "C"
    elif average>=50:
        return "D"
    else:
        return "F"


def analyze_students():


    rows = display_students()

    df=pd.DataFrame(
        rows,
        columns=["id","name","age","department","python_marks","database_marks","data_analysis_marks"]
    )

    average_python_marks = df["python_marks"].mean()
    average_database_marks = df["database_marks"].mean()
    average_data_analysis_marks = df["data_analysis_marks"].mean()

    highest_python_marks = df["python_marks"].max()
    lowest_python_marks = df["python_marks"].min()

    total_students = len(df)


     #for numpy now
    #to perform some numpy analysis we ned to convert marks into numpy array

    python_marks = df["python_marks"].to_numpy()

    avg=np.mean(python_marks)
    highest=np.max(python_marks)
    lowest=np.min(python_marks)

    standard_deviation=np.std(python_marks)



    #Display analysis
    print("Total Students:", total_students)
    print("Average Python Marks:", average_python_marks)
    print("Average Database Marks:", average_database_marks)
    print("Average Data Analysis Marks:", average_data_analysis_marks)
    print("Highest Python Marks:", highest_python_marks)
    print("Lowest Python Marks:", lowest_python_marks)

    print("NumPy Average:", avg)
    print("NumPy Highest:", highest)
    print("NumPy Lowest:", lowest)
    print("Standard Deviation:", standard_deviation)




def generate_report():

    rows = display_students()

    with open("student_report.txt", "w") as file:

        for i in rows:

            id, name, age, department, python_marks, database_marks, data_analysis_marks = i

            total_marks = python_marks + database_marks + data_analysis_marks
            average = total_marks / 3

            grade = calculate_result(
                python_marks,
                database_marks,
                data_analysis_marks
            )

            print("ID:", id)
            print("Name:", name)
            print("Age:", age)
            print("Department:", department)
            print("Python Marks:", python_marks)
            print("Database Marks:", database_marks)
            print("Data Analysis Marks:", data_analysis_marks)
            print("Total Marks:", total_marks)
            print("Average:", average)
            print("Grade:", grade)

            file.write(str(id) + "\n")
            file.write(str(name) + "\n")
            file.write(str(age)+ "\n")
            file.write(str(department)+ "\n")
            file.write(str(python_marks)+ "\n")
            file.write(str(database_marks)+ "\n")
            file.write(str(data_analysis_marks)+ "\n")
            file.write(str(total_marks)+ "\n")
            file.write(str(average)+ "\n")
            file.write(str(grade)+ "\n")

    print("Report generated successfully.")

#now we will read all data which is in our generated report file
def read_report():

    with open("student_report.txt","r") as f:
        read=f.read()

        print(read)



def main():

    create_database()


    while True:


        print("1:Add students")
        print("2:Display all students")
        print("3:Search Students")
        print("4:Analyze students")
        print("5:Generate report")
        print("6:Read report")
        print("7:Exit")

        choice=int(input("enter your choice."))

        if choice==1:
            print("your choice is add students so:")

            id=int(input("Enter Student ID:"))
            name=input("Enter Name:")
            age=int(input("Enter Age:"))
            department=input("Enter Department:")
            python_marks=int(input("Enter python marks:"))
            database_marks=(int(input("Enter database marks:")))
            data_analysis_marks=int(input("Enter data analysis marks:"))


            #calling function
            add_student(id, name, age, department, python_marks, database_marks, data_analysis_marks)

            print("student added successfullt")

        elif choice==2:
            print("your choice is display students so:")

            rows=display_students()

            for i in rows:
                id, name, age, department, python_marks, database_marks, data_analysis_marks = i


                print("ID:", id)
                print("Name:", name)
                print("Age:", age)
                print("Department:", department)
                print("Python Marks:", python_marks)
                print("Database Marks:", database_marks)
                print("Data Analysis Marks:", data_analysis_marks)




        elif choice == 3:
            print("Your choice is search student:")

            id= int(input("Enter Student ID: "))

            search_student(id)


        elif choice == 4:
            print("Your choice is analyze students:")

            analyze_students()

        elif choice == 5:
            print("Your choice is generate report:")

            generate_report()

        elif choice == 6:
            print("Your choice is read report:")

            read_report()


        elif choice == 7:
           print("Exiting program...")
           #while loops will end here
           break

        else:
          print("Invalid choice")


main()
    



