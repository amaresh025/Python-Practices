nums = [1, 2, 2, 3, 1, 4, 2]

indexs = {}

for i in nums:
    if i in indexs:
        indexs[i] = indexs[i] + [nums.index(i, indexs[i][-1] + 1)]

    else:
        indexs[i] = [nums.index(i)]

print(indexs)