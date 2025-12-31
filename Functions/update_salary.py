employees = [
    {"id": 1, "name": "Adam", "salary": 25000},
    {"id": 2, "name": "Bob", "salary": 30000},
    {"id": 3, "name": "Casey", "salary": 40000},
]


def update_salary(name, new_salary):
    for emp in employees:
        if emp["name"] == name:
            emp["salary"] = new_salary
            return True
    return False

print(update_salary("Adam", 45000))
print(employees)