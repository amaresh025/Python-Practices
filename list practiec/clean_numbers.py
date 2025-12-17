data = ["12", "7", "abc", "", "45", "9x", "30"]

result = []

for item in data:
    try:
        num = int(item)

        result.append(num)
    except:
        pass

print(result)    
