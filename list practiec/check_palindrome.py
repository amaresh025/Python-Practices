nums = [1, 2, 3, 2, 1]
is_palindrome = True

for i in range(len(nums)//2):
    if nums[i] != nums[len(nums)-1-i]:
        is_palindrome = False
print(is_palindrome)