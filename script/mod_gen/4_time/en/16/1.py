def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]
print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 10))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 20))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 30))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 40))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 50))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 60))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 70))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 80))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 90))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 100))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 110))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 120))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10], 130))
print(combinationSum4([1,2,3,4,5,6,7,8,9,10
