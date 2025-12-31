employees = [
    {"id": 1, "name": "Adam", "salary": 25000},
    {"id": 2, "name": "Bob", "salary": 30000},
    {"id": 3, "name": "Casey", "salary": 40000},
]

def find_emp(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
        
    return None

print(find_emp(1))
print(find_emp(5))
print(find_emp(3))
