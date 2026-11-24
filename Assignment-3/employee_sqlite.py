import sqlite3

class Employee:
    def __init__(self):
        self.con = sqlite3.connect("employee.db")
        self.cur = self.con.cursor()
        self.cur.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")
        self.con.commit()
    def add(self):
        emp_id = int(input("id: "))
        name = input("name: ")
        department = input("department: ")
        salary = float(input("salary: "))
        try:
            self.cur.execute(
                "INSERT INTO employee VALUES (?, ?, ?, ?)",
                (emp_id, name, department, salary)
            )
            self.con.commit()
            print("ok")
        except sqlite3.IntegrityError:
            print("id exists")
    def display(self):
        self.cur.execute("SELECT * FROM employee")
        records = self.cur.fetchall()
        if len(records) == 0:
            print("no records")
        else:
            for row in records:
                print(row)
    def search(self):
        emp_id = int(input("search: "))
        self.cur.execute(
            "SELECT * FROM employee WHERE id = ?",
            (emp_id,)
        )
        record = self.cur.fetchone()
        if record:
            print(record)
        else:
            print("not found")
    def update(self):
        emp_id = int(input("update id: "))
        self.cur.execute(
            "SELECT * FROM employee WHERE id = ?",
            (emp_id,)
        )
        record = self.cur.fetchone()
        if record:
            name = input("new name: ")
            department = input("new department: ")
            salary = float(input("new salary: "))
            self.cur.execute("""
UPDATE employee
SET name = ?, department = ?, salary = ?
WHERE id = ?
""", (name, department, salary, emp_id))
            self.con.commit()
            print("ok")
        else:
            print("not found")
    def delete(self):
        emp_id = int(input("delete id: "))
        self.cur.execute(
            "DELETE FROM employee WHERE id = ?",
            (emp_id,)
        )
        self.con.commit()
        if self.cur.rowcount > 0:
            print("ok")
        else:
            print("not found")
    def close(self):
        self.con.close()

employee = Employee()
while True:
    print("\n1. add")
    print("2. show")
    print("3. search")
    print("4. update")
    print("5. delete")
    print("6. exit")
    choice = input("choice: ")
    if choice == "1":
        employee.add()
    elif choice == "2":
        employee.display()
    elif choice == "3":
        employee.search()
    elif choice == "4":
        employee.update()
    elif choice == "5":
        employee.delete()
    elif choice == "6":
        print("bye")
        break
    else:
        print("invalid")

employee.close()
