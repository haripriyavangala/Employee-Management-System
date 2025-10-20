# Employee-Management-System
A simple yet powerful Employee Management System built using Python Flask and Pickle-based data storage. This project allows you to Add, Edit, Delete, Search, Sort, and View employees — all through a clean and modern web interface

# 🧑‍💼 Employee Management System (Flask + SQLite)

A simple yet powerful **Employee Management System** built using **Python Flask** and **SQLite**.  
It allows users to **Add**, **Edit**, **Delete**, **Search**, and **Sort Employees**, with a beautiful modern UI.  

---

## 🌟 Features

✅ Add new employees  
✅ Edit employee details  
✅ Delete employees  
✅ Search employees by **ID**, **Name**, **Role**, or **Salary**  
✅ Sort employees by **Name**, **Role**, **Salary**, or **ID**  
✅ Show all employees after filters  
✅ “Total Employees” counter  
✅ Beautiful responsive UI (modern CSS with glassmorphism effect)  

---

## 🧰 Tech Stack

| Layer | Technology |
|-------|-------------|
| **Frontend** | HTML5, CSS3 (Custom Gradient + Glassmorphism) |
| **Backend** | Python (Flask Framework) |
| **Database** | SQLite |
| **Templating** | Jinja2 |
| **Version Control** | Git & GitHub |

---

employee-management-system/
│
├── app.py                  # Main Flask backend
├── employees.db            # SQLite Database (auto-created)
│
├── static/
│   └── style.css           # CSS file for styling
│
├── templates/
│   ├── index.html          # Home page (Employee list)
│   ├── edit_employee.html  # Edit employee form
│
└── README.md

Create a virtual environment: python -m venv venv

Activate the environment:
On Windows: venv\Scripts\activate
On Mac/Linux: source venv/bin/activate

Install dependencies: pip install flask

Run the Flask app: python app.py


View Here:

http://127.0.0.1:5000/

