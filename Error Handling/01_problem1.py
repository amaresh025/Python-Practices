def check_age(age):
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
        "age": age
    }

print(check_age("he"))
print(check_age("83"))
print(check_age("h32"))
print(check_age(12))