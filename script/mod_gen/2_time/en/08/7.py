def maxRotateFunction(nums):
    n = len(nums)
    sum_all = sum(nums)
    F = 0
    for i in range(n):
        F += i*nums[i]
    max_F = F
    for i in range(1, n):
        F = F + sum_all - n*nums[n-i]
        if F > max_F:
            max_F = F
    return max_F
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10]))
