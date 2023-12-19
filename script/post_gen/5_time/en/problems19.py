Synthesizing 10/10 solutions

=======
Suggestion 1

def canIWin(maxChoosableInteger, desiredTotal):
    if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    memo = {}
    def dfs(nums, total):
        if nums[-1] >= total:
            return True
        key = tuple(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not dfs(nums[:i] + nums[i+1:], total - nums[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return dfs(list(range(1, maxChoosableInteger + 1)), desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))

=======
Suggestion 2

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
        return False
    return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

=======
Suggestion 3

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal: return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal: return False
    def helper(nums, desiredTotal):
        if nums[-1] >= desiredTotal: return True
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i]): return True
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

=======
Suggestion 4

def canIWin(maxChoosableInteger, desiredTotal):
    return True

=======
Suggestion 5

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1) / 2) < desiredTotal:
        return False
    memo = {}
    def dfs(used, total):
        if total <= 0:
            return False
        key = str(used)
        if key in memo:
            return memo[key]
        for i in range(1, maxChoosableInteger + 1):
            if used & (1 << i) == 0:
                if not dfs(used | (1 << i), total - i):
                    memo[key] = True
                    return True
        memo[key] = False
        return False
    return dfs(0, desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(18, 79))
print(canIWin(4, 6))
print(canIWin(20, 210))

=======
Suggestion 6

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) / 2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if nums[-1] >= desiredTotal:
            return True
        if tuple(nums) in memo:
            return memo[tuple(nums)]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i + 1:], desiredTotal - nums[i], memo):
                memo[tuple(nums)] = True
                return True
        memo[tuple(nums)] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 2))
print(canIWin(10, 3))
print(canIWin(10, 4))
print(canIWin(10, 5))
print(canIWin(10, 6))
print(canIWin(10, 7))
print(canIWin(10, 8))
print(canIWin(10, 9))
print(canIWin(10, 10))
print(canIWin(10, 11))
print(canIWin(10, 12))
print(canIWin(10, 13))
print(canIWin(10, 14))
print(canIWin(10, 15))
print(canIWin(10, 16))
print(canIWin(10, 17))
print(canIWin(10, 18))
print(canIWin(10, 19))
print(canIWin(10, 20))
print(canIWin(10, 21))
print(canIWin(10, 22))
print(canIWin(10, 23))
print(canIWin(10, 24))
print(canIWin(10, 25))
print(canIWin(10, 26))
print(canIWin(10, 27))
print(canIWin(10, 28))
print(canIWin(10, 29))
print(canIWin(10, 30))
print(canIWin(10, 31

=======
Suggestion 7

def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal: return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal: return False
    def can_win(choices, desiredTotal, cache):
        if choices[-1] >= desiredTotal: return True
        key = str(choices)
        if key in cache: return cache[key]
        for i in range(len(choices)):
            if not can_win(choices[:i] + choices[i+1:], desiredTotal - choices[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return can_win(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

=======
Suggestion 8

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0 or maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False

    def helper(nums, desiredTotal, memo):
        if memo[nums] != None:
            return memo[nums]
        if nums[-1] >= desiredTotal:
            return True
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                memo[nums] = True
                return True
        memo[nums] = False
        return False

    memo = {}
    nums = [i for i in range(1, maxChoosableInteger + 1)]
    return helper(tuple(nums), desiredTotal, memo)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 2))
print(canIWin(10, 3))
print(canIWin(10, 4))
print(canIWin(10, 5))
print(canIWin(10, 6))
print(canIWin(10, 7))
print(canIWin(10, 8))
print(canIWin(10, 9))
print(canIWin(10, 10))
print(canIWin(10, 11))
print(canIWin(10, 12))
print(canIWin(10, 13))
print(canIWin(10, 14))
print(canIWin(10, 15))
print(canIWin(10, 16))
print(canIWin(10, 17))
print(canIWin(10, 18))
print(canIWin(10, 19))
print(canIWin(10, 20))
print(canIWin(10, 21))
print(canIWin(10, 22))
print(canIWin(10, 23))
print(canIWin(10, 24))
print(canIWin(10, 25))
print(canIWin(10, 26))
print(canIWin(10, 27))
print(canIWin(10, 28))
print(canIWin(10, 29))

=======
Suggestion 9

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 == desiredTotal:
        return maxChoosableInteger % 2 == 1
    return helper(desiredTotal, [False] * (maxChoosableInteger + 1), {})

=======
Suggestion 10

def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger+1)*maxChoosableInteger < desiredTotal*2:
        return False
    def helper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key in cache:
            return cache[key]
        for i in range(len(nums)):
            if not helper(nums[:i]+nums[i+1:], desiredTotal-nums[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return helper(list(range(1, maxChoosableInteger+1)), desiredTotal, {})
