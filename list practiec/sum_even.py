nums = [1, 4, 7, 8, 10, 3]
sum_of_even = 0
for i in nums:
    if i % 2 == 0:
        sum_of_even = sum_of_even + i
    
print(sum_of_even)