data = {"name": "Rohit", "age": "8d3"}

def check_data(d):
    try:
        age = d["age"]
    except KeyError:
        return {
            "status": "error",
            "message": "Age is required"
        }

    return {
        "status": "success",
        "age": age
    }


print(check_data(data))