import sqlite3


def create_database():
    connection = sqlite3.connect("students_management.db")
    cursor = connection.cursor()

    cursor.execute("""

        CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        department TEXT,
        python_marks REAL,
        database_marks REAL,
        data_analysis_marks REAL
        
        );

""")
    connection.commit()
    connection.close()


def add_student(id, name, age, department, python_marks, database_marks, data_analysis_marks):

    conn = sqlite3.connect("students_management.db")
    cursor = conn.cursor()

    cursor.execute("""
                INSERT INTO students(id,name,age,department,python_marks,database_marks,data_analysis_marks)
                VALUES(?,?,?,?,?,?,?)
""", (
        id, name, age, department, python_marks, database_marks, data_analysis_marks,
    ))

    conn.commit()
    conn.close()


def display_students():

    conn = sqlite3.connect("students_management.db")
    cursor = conn.cursor()

    cursor.execute("""
          SELECT * FROM students
          ORDER BY name;

""")

    rows = cursor.fetchall()
    conn.close()
    return rows


def search_student(id):

    conn = sqlite3.connect("students_management.db")
    cursor = conn.cursor()

    cursor.execute("""
              SELECT * FROM students
              WHERE id=?
""", (id,))

    row = cursor.fetchone()

    if row is None:
        print("student not found")
    else:
        print("student found successfully")

    conn.close()


def calculate_result(python_marks, database_marks, data_analysis_marks):

    total_marks = python_marks + database_marks + data_analysis_marks

    average = total_marks / 3

    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"