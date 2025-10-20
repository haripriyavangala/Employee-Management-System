from flask import Flask, render_template, request, redirect, url_for
import pickle
import os

app = Flask(__name__)
DATA_FILE = 'employees.pkl'

# ------------------ Helper functions ------------------
def load_data():
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return []
    return []

def save_data(employees):
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(employees, f)

# ------------------ Load initial data ------------------
employees = load_data()

# If file is empty, initialize some demo data
if not employees:
    employees = [
        {"id": 1, "name": "Hari Priya", "role": "Software Developer", "salary": 60000},
        {"id": 2, "name": "John Doe", "role": "Data Analyst", "salary": 55000},
        {"id": 3, "name": "Vangala", "role": "Cloud Engineer", "salary": 70000},
    ]
    save_data(employees)

# ------------------ Routes ------------------
@app.route('/')
def index():
    search_query = request.args.get('search', '').strip().lower()
    sort_option = request.args.get('sort', 'id')

    # Start with all employees
    filtered = employees.copy()

    # 🔍 Apply search filter
    if search_query:
        filtered = [
            e for e in filtered
            if search_query in str(e["id"]).lower()
            or search_query in e["name"].lower()
            or search_query in e["role"].lower()
        ]

    # 🔽 Apply sorting
    if sort_option == "id":
        filtered.sort(key=lambda x: x["id"])
    elif sort_option == "name":
        filtered.sort(key=lambda x: x["name"].lower())
    elif sort_option == "role":
        filtered.sort(key=lambda x: x["role"].lower())
    elif sort_option == "salary":
        filtered.sort(key=lambda x: float(x["salary"]))

    # Pass search and sort back to template for state
    return render_template('index.html', employees=filtered, total=len(filtered),
                           search_query=search_query, show_all=(search_query != ""))


@app.route('/show_all')
def show_all():
    """Clears any filters and shows all employees."""
    return redirect(url_for('index'))


@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']
    role = request.form['role']
    salary = request.form['salary']

    if name and role and salary:
        new_id = max([e["id"] for e in employees], default=0) + 1
        new_emp = {"id": new_id, "name": name, "role": role, "salary": int(salary)}
        employees.append(new_emp)
        save_data(employees)

    return redirect('/')


@app.route('/edit/<int:emp_id>', methods=['GET', 'POST'])
def edit_employee(emp_id):
    emp = next((e for e in employees if e["id"] == emp_id), None)
    if not emp:
        return redirect('/')

    if request.method == 'POST':
        emp["name"] = request.form["name"]
        emp["role"] = request.form["role"]
        emp["salary"] = int(request.form["salary"])
        save_data(employees)
        return redirect('/')
    return render_template('edit_employee.html', emp=emp)


@app.route('/delete/<int:emp_id>')
def delete_employee(emp_id):
    global employees
    employees = [e for e in employees if e["id"] != emp_id]
    save_data(employees)
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
