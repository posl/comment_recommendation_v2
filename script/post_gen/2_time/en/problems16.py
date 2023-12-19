Synthesizing 10/10 solutions

=======
Suggestion 1

def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]

    return dp[target]

=======
Suggestion 2

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(len(nums)):
            if nums[j] <= i:
                dp[i] += dp[i - nums[j]]
    return dp[-1]

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))

nums = [9]
target = 3
print(combinationSum4(nums, target))

=======
Suggestion 3

def combinationSum4(nums, target):
    dp = [0 for _ in range(target + 1)]
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]

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
print(combinationSum4([1,2,

=======
Suggestion 4

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target + 1):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                dp[i] += dp[i - nums[j]]
    return dp[target]

=======
Suggestion 5

def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i-num >= 0:
                dp[i] += dp[i-num]
    return dp[target]

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))

=======
Suggestion 6

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

=======
Suggestion 7

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

=======
Suggestion 8

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[-1]

print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))

=======
Suggestion 9

def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]
    return dp[target]

print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))
print(combinationSum4([1,2,3], 32))
print(combinationSum4([1,2,3], 32))

=======
Suggestion 10

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1,target+1):
        for j in range(len(nums)):
            if i - nums[j] >= 0:
                dp[i] += dp[i - nums[j]]
    return dp[target]

print(combinationSum4([1,2,3],4))
print(combinationSum4([9],3))
print(combinationSum4([1,2,3],32))
print(combinationSum4([1,2,3],32))
print(combinationSum4([1,2,3],32
