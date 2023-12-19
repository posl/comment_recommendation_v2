Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for n in nums:
            if i-n >= 0:
                dp[i] += dp[i-n]
    return dp[target]

print(combinationSum4([1,2,3], 4))
print(combinationSum4([9], 3))

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

=======
Suggestion 3

def combinationSum4(nums, target):
    dp = [0] * (target+1)
    dp[0] = 1
    for i in range(1, target+1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i-num]
    return dp[target]

=======
Suggestion 4

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

nums = [1,2,3]
target = 4
result = combinationSum4(nums, target)
print(result)

=======
Suggestion 5

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

=======
Suggestion 6

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for j in range(len(nums)):
            if i >= nums[j]:
                dp[i] += dp[i - nums[j]]
    return dp[target]

=======
Suggestion 7

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(1, target + 1):
        for num in nums:
            if i >= num:
                dp[i] += dp[i - num]
    return dp[target]

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

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))

nums = [9]
target = 3
print(combinationSum4(nums, target))

=======
Suggestion 9

def combinationSum4(nums, target):
    dp = [0] * (target + 1)
    dp[0] = 1
    for i in range(target + 1):
        for num in nums:
            if i - num >= 0:
                dp[i] += dp[i - num]
    return dp[target]

nums = [1,2,3]
target = 4
print(combinationSum4(nums, target))
