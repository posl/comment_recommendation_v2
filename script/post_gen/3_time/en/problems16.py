Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

=======
Suggestion 2

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

print(combinationSum4([1,2,3], 4))

=======
Suggestion 3

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]

=======
Suggestion 4

def combinationSum4(nums, target):
    dp = [0 for i in range(target+1)]
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]
    return dp[target]
        
print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1,2,3,4], 5))

=======
Suggestion 5

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[-1]

=======
Suggestion 6

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if num <= i:
                dp[i] += dp[i - num]
    return dp[-1]

print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1,2,3], 32))

=======
Suggestion 7

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, len(dp)):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]

nums = [1, 2, 3]
target = 4
print(combinationSum4(nums, target))

nums = [9]
target = 3
print(combinationSum4(nums, target))

=======
Suggestion 8

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
print(combinationSum4([1,2,3], 26))
print(combinationSum4([1,2,3], 27))
print(combinationSum4([1,2,3], 28))
print(combinationSum4([1,2,3], 29))
print(combinationSum4([1,2,3], 30))
print(combinationSum4([1,2,3],
