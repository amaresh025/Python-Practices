employees = [
    {"id": 1, "name": "Adam", "salary": 25000},
    {"id": 2, "name": "Bob", "salary": 30000},
    {"id": 3, "name": "Casey", "salary": 40000},
]
def min_salary_emp(min_salary):
    result = []
    for emp in employees:
        if emp["salary"] >= min_salary:
            result.append(emp)

    return result

print(min_salary_emp(30000))