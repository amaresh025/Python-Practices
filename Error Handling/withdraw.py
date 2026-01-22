def withdraw(balance, amount):
    try:
        balance = int(balance)
        amount = int(amount)
    except (ValueError, TypeError):
        return {
            "status": "error", 
            "message": "balance and amount must be a number"
        }
    if balance < 0 or amount < 0:
        return {
            "status": "error", 
            "message": "balance and amount must be > 0"
        }
    if balance < amount:
        return{
            "status": "error",
            "message": "balance must be >= amount"
        }

    return {
        "status": "success",
        "new_balance": balance - amount
    }
            


print(withdraw(10,10))
print(withdraw(50,10))
print(withdraw(10,50))
print(withdraw("eh", 10))


