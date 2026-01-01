employees = [
    {"id": 1, "name": "Adam", "salary": 25000, "dept": "HR"},
    {"id": 2, "name": "Bob", "salary": 30000, "dept": "IT"},
    {"id": 3, "name": "Casey", "salary": 40000, "dept": "IT"},
    {"id": 4, "name": "David", "salary": 80000, "dept": "HR"},
    {"id": 5, "name": "Eva", "salary": 50000, "dept": "Finance"},
]

def dept_emp(dept_name):
    counts = 0
    for emp in employees:
        if emp["dept"] == dept_name:
            counts += 1

    return counts

print(dept_emp("HR"))


def high_salary_emp():
    max_salary = 0
    for emp in employees:
        if emp["salary"] >= max_salary:
            max_salary = emp["salary"]
            high_salary_employee = emp

    return high_salary_employee
            
print(high_salary_emp())


def emp_dept():
    dept = {"HR" : [], "IT" : [], "Finance" : []}
    for emp in employees:
        if emp["dept"] == "IT":
            dept["IT"].append(emp)
        

        elif emp["dept"] == "HR":
            dept["HR"].append(emp)
        elif emp["dept"] == "Finance":
            dept["Finance"].append(emp)
    return dept


print(emp_dept())

def salary_inc(dept_name):
    counts = 0
    for emp in employees:
        if emp["dept"] == dept_name:
            emp["salary"] += emp["salary"] * 10 / 100
            counts += 1

    return counts

print(salary_inc("IT"))


