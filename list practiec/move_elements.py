nums = [0, 1, 0, 3, 12]
result = []
zero_counts = 0
for i in nums:
    if i == 0:
        zero_counts += 1

    else:
        result.append(i)

for _ in range(zero_counts):
    result.append(0)
    
print(result)
