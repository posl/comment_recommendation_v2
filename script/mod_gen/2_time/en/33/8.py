def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [{} for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            if d in dp[j]:
                dp[i][d] = dp[j][d] + 1
                ans += dp[j][d]
            else:
                dp[i][d] = 1
    return ans
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([2,4,6,8,10,12]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26,28]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]))
print(numberOfArithmeticSlices([2,4,6,8,10,
