nums = [10, 5, 8, 20, 15]
second_max = nums[0]
maximum = nums[0]
for i in nums[1:]:
    if maximum < i:
        second_max = maximum
        maximum = i
    elif i < maximum and i > second_max:
        second_max = i
    


print(second_max)