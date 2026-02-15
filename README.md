# 🏦 BANK MANAGEMENT SYSTEM
### A Python & MySQL Based Console Banking Application

---

## 📖 PROJECT OVERVIEW

The **Bank Management System** is a console-based application developed using **Python** and **MySQL**.  
This project demonstrates how to connect Python with a MySQL database and perform real-time database operations using SQL queries.

The system allows users to perform essential banking operations such as:

- Creating a new bank account
- Viewing account details
- Checking account balance
- Depositing money
- Withdrawing money

All account data is securely stored in a MySQL database.

---

## 🎯 OBJECTIVE

The main objective of this project is to:

- Understand database connectivity in Python
- Perform CRUD operations using SQL
- Implement real-world banking logic
- Build a structured menu-driven program
- Practice backend logic development

---

## 🛠 TECHNOLOGIES USED

- **Python 3**
- **MySQL Server**
- **mysql-connector-python**
- **SQL (Structured Query Language)**

---

# ⚙ HOW THE PROGRAM WORKS

1. The program connects to the MySQL database.

2. A cursor object is created to execute SQL queries.

3. The user is shown a menu with different banking options.

4. The user selects an option from the menu.

5. Based on the selected option, appropriate SQL queries are executed:
   - INSERT (for creating accounts)
   - SELECT (for viewing details and checking balance)
   - UPDATE (for deposit and withdrawal)

6. Any changes made to the database are committed using `commit()`.

7. The program runs inside a loop and continues showing the menu until the


# ⚠ REQUIREMENTS

- MySQL Server must be running.
- The database must be created before running the program.
- Correct MySQL username and password must be provided in the connection settings.

---

# 🔮 FUTURE IMPROVEMENTS

- Add login authentication system.
- Implement transaction history tracking.
- Add transfer money feature between accounts.
- Develop a GUI using Tkinter.
- Improve error and exception handling.
- Create an admin panel for managing accounts.



