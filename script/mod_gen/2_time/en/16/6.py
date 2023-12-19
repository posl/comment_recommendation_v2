def combinationSum4(nums, target):
    nums.sort()
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if n > i:
                break
            dp[i] += dp[i-n]
    return dp[-1]
print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1,2,3], 32))
print(combinationSum4([1,2,3], 0))
print(combinationSum4([1,2,3], 1))
print(combinationSum4([1,2,3], 2))
print(combinationSum4([1,2,3], 3))
print(combinationSum4([1,2,3], 5))
print(combinationSum4([1,2,3], 6))
print(combinationSum4([1,2,3], 7))
print(combinationSum4([1,2,3], 8))
print(combinationSum4([1,2,3], 9))
print(combinationSum4([1,2,3], 10))
print(combinationSum4([1,2,3], 11))
print(combinationSum4([1,2,3], 12))
print(combinationSum4([1,2,3], 13))
print(combinationSum4([1,2,3], 14))
print(combinationSum4([1,2,3], 15))
print(combinationSum4([1,2,3], 16))
print(combinationSum4([1,2,3], 17))
print(combinationSum4([1,2,3], 18))
print(combinationSum4([1,2,3], 19))
print(combinationSum4([1,2,3], 20))
print(combinationSum4([1,2,3], 21))
print(combinationSum4([1,2,3], 22))
print(combinationSum4([1,2,3], 23))
print(combinationSum4([1,2,3], 24))
print(combinationSum4([1,2,3], 25))
print(combinationSum4([1,2
