import sqlite3
import pandas as pd

con = sqlite3.connect("employee.db")
cur = con.cursor()
cur.execute("""
CREATE TABLE IF NOT EXISTS employee(
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
con.commit()

def add_employee():
    id = int(input("id: "))
    name = input("name: ")
    department = input("department: ")
    salary = float(input("salary: "))
    try:
        cur.execute(
            "INSERT INTO employee VALUES (?, ?, ?, ?)",
            (id, name, department, salary)
        )
        con.commit()
        print("ok")
    except sqlite3.IntegrityError:
        print("id exists")

def display_employee():
    df = pd.read_sql_query("SELECT * FROM employee", con)
    if df.empty:
        print("no records")
    else:
        print(df)

def search_employee():
    id = int(input("search: "))
    df = pd.read_sql_query(
        "SELECT * FROM employee WHERE id = ?",
        con,
        params=(id,)
    )
    if df.empty:
        print("not found")
    else:
        print(df)

def update_employee():
    id = int(input("update id: "))
    cur.execute("SELECT * FROM employee WHERE id = ?", (id,))
    result = cur.fetchone()
    if result:
        name = input("new name: ")
        department = input("new department: ")
        salary = float(input("new salary: "))
        cur.execute("""
UPDATE employee
SET name = ?, department = ?, salary = ?
WHERE id = ?
""", (name, department, salary, id))
        con.commit()
        print("ok")
    else:
        print("not found")

def delete_employee():
    id = int(input("delete id: "))
    cur.execute("SELECT * FROM employee WHERE id = ?", (id,))
    result = cur.fetchone()
    if result:
        cur.execute("DELETE FROM employee WHERE id = ?", (id,))
        con.commit()
        print("ok")
    else:
        print("not found")

while True:
    print("\n1. add")
    print("2. show")
    print("3. search")
    print("4. update")
    print("5. delete")
    print("6. exit")
    choice = input("choice: ")
    if choice == "1":
        add_employee()
    elif choice == "2":
        display_employee()
    elif choice == "3":
        search_employee()
    elif choice == "4":
        update_employee()
    elif choice == "5":
        delete_employee()
    elif choice == "6":
        print("bye")
        break
    else:
        print("invalid")

con.close()