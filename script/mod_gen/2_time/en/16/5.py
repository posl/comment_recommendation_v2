def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]
print(combinationSum4([1, 2, 3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1, 2, 3, 4], 5))
print(combinationSum4([1, 2, 3, 4], 8))
print(combinationSum4([1, 2, 3, 4], 12))
print(combinationSum4([1, 2, 3, 4], 16))
print(combinationSum4([1, 2, 3, 4], 20))
print(combinationSum4([1, 2, 3, 4], 24))
print(combinationSum4([1, 2, 3, 4], 28))
print(combinationSum4([1, 2, 3, 4], 32))
print(combinationSum4([1, 2, 3, 4], 36))
print(combinationSum4([1, 2, 3, 4], 40))
print(combinationSum4([1, 2, 3, 4], 44))
print(combinationSum4([1, 2, 3, 4], 48))
print(combinationSum4([1, 2, 3, 4], 52))
print(combinationSum4([1, 2, 3, 4], 56))
print(combinationSum4([1, 2, 3, 4], 60))
print(combinationSum4([1, 2, 3, 4], 64))
print(combinationSum4([1, 2, 3, 4], 68))
print(combinationSum4([1, 2, 3, 4], 72))
print(combinationSum4([1, 2, 3, 4], 76))
print(combinationSum4([1, 2, 3, 4], 80
