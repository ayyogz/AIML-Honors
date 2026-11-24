import os
import pandas as pd
file_name = "employee.csv"
columns = ["id", "name", "department", "salary"]
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
else:
    df = pd.DataFrame(columns=columns)

def save_data():
    df.to_csv(file_name, index=False)
def add_employee():
    global df
    emp_id = int(input("id: "))
    if emp_id in df["id"].values:
        print("id exists")
        return
    name = input("name: ")
    department = input("department: ")
    salary = float(input("salary: "))
    new_employee = pd.DataFrame(
        [[emp_id, name, department, salary]],
        columns=columns
    )
    df = pd.concat([df, new_employee], ignore_index=True)
    save_data()
    print("ok")

def display_employee():
    if df.empty:
        print("no records")
    else:
        print(df.to_string(index=False))

def search_employee():
    emp_id = int(input("search: "))
    result = df[df["id"] == emp_id]
    if result.empty:
        print("not found")
    else:
        print(result.to_string(index=False))
def update_employee():
    global df
    emp_id = int(input("update id: "))
    if emp_id not in df["id"].values:
        print("not found")
        return
    name = input("new name: ")
    department = input("new department: ")
    salary = float(input("new salary: "))
    df.loc[df["id"] == emp_id, "name"] = name
    df.loc[df["id"] == emp_id, "department"] = department
    df.loc[df["id"] == emp_id, "salary"] = salary
    save_data()
    print("ok")

def delete_employee():
    global df
    emp_id = int(input("delete id: "))
    if emp_id not in df["id"].values:
        print("not found")
        return
    df = df[df["id"] != emp_id]
    save_data()
    print("ok")
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
