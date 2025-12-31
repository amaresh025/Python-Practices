employees = [
    {"id": 1, "name": "Adam", "salary": 25000},
    {"id": 2, "name": "Bob", "salary": 30000},
    {"id": 3, "name": "Casey", "salary": 40000},
]

def emp_higher_salary(data):
    result = []
    for emp in data:
        if emp["salary"] >= 30000:
            result.append(emp)
    return result
print(emp_higher_salary(employees))