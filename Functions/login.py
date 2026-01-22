def login(name: str, password: str) -> dict:
    
    if name == "admin" and password == "123":
        return {"status": "success"}
    

    return {
        "status": "error",
        "message": "something wrong"
    }

print(login("amar", "123"))
print(login("admin", "123"))