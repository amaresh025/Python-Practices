data = [1, 2, 2, 3, 1, 4]

result = []

for item in data:
    if item not in result:
        result.append(item)

print(result)
