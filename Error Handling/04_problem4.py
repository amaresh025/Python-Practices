
def check_data(data):
    try:
        age = data["age"]
        name = data["name"]
    except KeyError:
        return {
            "status": "error",
            "message": "Required field is missing"
        }
    if not name.strip():
        return {
            "status": "error",
            "message": "Name is required"
        }
    try:
        age = int(age)
    except ValueError:
        return {
            "status": "error",
            "message": "Age must be a number"
        }
    
    if age < 18:
        return {
            "status": "error",
            "message": "Age must be >= 18"
        }
    
    return {
        "status": "success",
        "data": {
        "age": age,
        "name": name
        }
    }


d = {"name": "8", "age": "34"}

print(check_data(d))