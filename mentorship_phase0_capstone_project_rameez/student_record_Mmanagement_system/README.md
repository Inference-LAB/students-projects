# 🎓 Student Record Management System

A command-line based Student Record Management System built with **Python**, **PostgreSQL**, and **SQLAlchemy ORM**.

This project was developed as a capstone project to demonstrate database connectivity, CRUD operations, file handling, project organization, and exception handling.

---

# 🚀 Features

- PostgreSQL Database
- SQLAlchemy ORM
- Student Management
- Course Management
- Enrollment Management
- Full CRUD Operations
- Export Tables to CSV
- Custom Exceptions
- Environment Variables using `.env`
- Clean Project Structure
- Menu Driven CLI

---

# 📂 Project Structure

```
student_record_management_system/
│
├── database.py
├── models.py
├── crud.py
├── main.py
├── .env
├── requirements.txt
│
├── exports/
│   └── exports_csv.py
│
├── README.md
└── .gitignore
```

---

# 🗄️ Database Tables

## Students

- student_id
- name
- roll_number
- email
- department
- semester
- cgpa

---

## Courses

- course_id
- course_name
- course_code
- credit_hours

---

## Enrollments

- id
- student_id
- course_id
- grade

---

# ⚙️ Technologies Used

- Python
- PostgreSQL
- SQLAlchemy ORM
- python-dotenv
- CSV Module

---

# 📦 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

The project uses the following Python libraries:

- SQLAlchemy
- psycopg2
- python-dotenv

# 🔐 Environment Variables

Create a `.env` file.

Example:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/student_record_management_system
```

---

# ▶️ How to Run

Run the application:

```bash
python main.py
```

---

# 📌 Menu

```
1. Create Student
2. View Students
3. Update Student
4. Delete Student

5. Create Course
6. View Courses
7. Update Course
8. Delete Course

9. Enroll Student
10. View Enrollments
11. Update Enrollment
12. Delete Enrollment

13. Export Table To CSV

0. Exit
```

---

# 📤 Export to CSV

The application can export any table to CSV.

Available exports:

- Students
- Courses
- Enrollments

Generated files:

- students.csv
- courses.csv
- enrollments.csv

---

# 📚 Concepts Demonstrated

- PostgreSQL
- SQLAlchemy ORM
- Database Sessions
- CRUD Operations
- Python Functions
- Exception Handling
- Custom Exceptions
- File Handling
- CSV Export
- Project Structure
- Environment Variables

---

# 👨‍💻 Author

**Rameez Raja**

BS Software Engineering

NFC Institute of Engineering and Technology

Pakistan

---

# 📄 License

This project is created for learning and educational purposes.