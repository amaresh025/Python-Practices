nums = [1, 1, 2, 3, 3, 3, 4, 4]
counts = {}
result = {"once":[], "twice":[], "many":[]}

for i in nums:
    if i in counts:
        counts[i] = counts[i] + 1
            
    else:
        counts[i] = 1

for i in counts:
    if counts[i] == 1:
        result["once"].append(i)
    elif counts[i] == 2:
        result["twice"].append(i)
    else:
        result["many"].append(i)

print(result)