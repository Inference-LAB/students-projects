# Mini Student Result Management System

## Description

The Mini Student Result Management System is a command-line Python program used to manage student records and results.

The system uses **SQLite** to store student information and **Pandas** and **NumPy** to perform student data analysis.

## Features

* Add new students
* Display all students
* Search for a student by ID
* Calculate total marks, average, and overall grade
* Analyze student marks using Pandas
* Perform numerical analysis using NumPy
* Generate a student report
* Read the generated report

## Subjects

The system stores marks for three subjects:

* Python
* Database
* Data Analysis

Marks are stored between **0 and 100**.

## Grading System

| Average Marks | Grade |
| ------------- | ----- |
| 90–100        | A+    |
| 80–89         | A     |
| 70–79         | B     |
| 60–69         | C     |
| 50–59         | D     |
| Below 50      | F     |

The grade is the **overall grade** of the student based on the average of the three subjects.

## Technologies Used

* Python
* SQLite
* Pandas
* NumPy

## Project Structure

```text
Student Result Management System/
│
├── database.py
├── main.py
├── students_management.db
├── student_report.txt
└── README.md
```

### database.py

Contains the database-related functions:

* `create_database()`
* `add_student()`
* `display_students()`
* `search_student()`

### main.py

Contains the main program functions:

* `calculate_result()`
* `analyze_students()`
* `generate_report()`
* `read_report()`
* `main()`

## How to Run

1. Make sure Python is installed.
2. Install Pandas and NumPy if they are not already installed.
3. Run `main.py`.

```bash
python main.py
```

## Main Menu

```text
1. Add Student
2. Display All Students
3. Search Student
4. Analyze Students
5. Generate Report
6. Read Report
7. Exit
```

## Database

Student information is stored in an SQLite database named:

```text
students_management.db
```

The `students` table contains:

```text
id
name
age
department
python_marks
database_marks
data_analysis_marks
```

## Reports

The `Generate Report` option creates:

```text
student_report.txt
```

The report contains each student's:

* ID
* Name
* Age
* Department
* Subject marks
* Total marks
* Average marks
* Overall grade

The `Read Report` option displays the saved report in the terminal.
