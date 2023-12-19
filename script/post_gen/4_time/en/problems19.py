Synthesizing 10/10 solutions

=======
Suggestion 1

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    nums = [i for i in range(1, maxChoosableInteger + 1)]
    return dfs(nums, desiredTotal, {})

=======
Suggestion 2

def canIWin(maxChoosableInteger, desiredTotal):
    def helper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in cache:
            return cache[key]
        for i, num in enumerate(nums):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - num, cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 150))
print(canIWin(10, 300))
print(canIWin(20, 200))
print(canIWin(20, 210))
print(canIWin(20, 300))
print(canIWin(20, 310))
print(canIWin(20, 400))
print(canIWin(20, 410))
print(canIWin(20, 500))
print(canIWin(20, 510))
print(canIWin(20, 600))
print(canIWin(20, 610))
print(canIWin(20, 700))
print(canIWin(20, 710))
print(canIWin(20, 800))
print(canIWin(20, 810))
print(canIWin(20, 900))
print(canIWin(20, 910))
print(canIWin(20, 1000))
print(canIWin(20, 1010))
print(canIWin(20, 1100))
print(canIWin(20, 1110))
print(canIWin(20, 1200))
print(canIWin(20, 1210))
print(canIWin(20, 1300))
print(canIWin(20, 1310))
print(canIWin(20, 1400))
print(canIWin(20, 1410))
print(canIWin

=======
Suggestion 3

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if nums[-1] >= desiredTotal:
            return True
        if str(nums) in memo:
            return memo[str(nums)]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i], memo):
                memo[str(nums)] = True
                return True
        memo[str(nums)] = False
        return False
    return helper([i for i in range(1, maxChoosableInteger + 1)], desiredTotal, {})

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(20, 200))
print(canIWin(20, 210))
print(canIWin(20, 211))
print(canIWin(20, 300))
print(canIWin(20, 301))
print(canIWin(20, 302))
print(canIWin(20, 303))
print(canIWin(20, 304))
print(canIWin(20, 305))
print(canIWin(20, 306))
print(canIWin(20, 307))
print(canIWin(20, 308))
print(canIWin(20, 309))
print(canIWin(20, 310))
print(canIWin(20, 311))
print(canIWin(20, 312))
print(canIWin(20, 313))
print(canIWin(20, 314))
print(canIWin(20, 315))
print(canIWin(20, 316))
print(canIWin(20, 317))
print(canIWin(20, 318))
print(canIWin(20, 319))
print(canIWin(20, 320))
print(canIWin(20, 321))
print(canIWin(20, 322))
print(canIWin(20, 323))
print(canIWin(20, 324))
print(canIWin(20, 325))
print(canIWin(20

=======
Suggestion 4

def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False

    def helper(remain, used, desiredTotal, cache):
        if used in cache:
            return cache[used]
        for i in range(1, maxChoosableInteger + 1):
            cur = 1 << (i - 1)
            if cur & used == 0:
                if remain <= i or not helper(remain - i, cur | used, desiredTotal, cache):
                    cache[used] = True
                    return True
        cache[used] = False
        return False
    return helper(desiredTotal, 0, desiredTotal, {})

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 55))
print(canIWin(10, 54))
print(canIWin(10, 56))
print(canIWin(10, 100))
print(canIWin(10, 101))
print(canIWin(10, 102))
print(canIWin(10, 103))
print(canIWin(10, 104))
print(canIWin(10, 105))
print(canIWin(10, 106))
print(canIWin(10, 107))
print(canIWin(10, 108))
print(canIWin(10, 109))
print(canIWin(10, 110))
print(canIWin(10, 111))
print(canIWin(10, 112))
print(canIWin(10, 113))
print(canIWin(10, 114))
print(canIWin(10, 115))
print(canIWin(10, 116))
print(canIWin(10, 117))
print(canIWin(10, 118))
print(canIWin(10, 119))
print(canIWin(10, 120))
print(canIWin(10, 121))
print

=======
Suggestion 5

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger * (maxChoosableInteger + 1) // 2 < desiredTotal:
        return False
    dp = {}
    def dfs(used, desiredTotal):
        if used in dp:
            return dp[used]
        for i in range(maxChoosableInteger):
            cur = 1 << i
            if cur & used == 0:
                if desiredTotal <= i + 1 or not dfs(used | cur, desiredTotal - i - 1):
                    dp[used] = True
                    return True
        dp[used] = False
        return False
    return dfs(0, desiredTotal)

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
print(canIWin(10, 20))
print(canIWin(10, 30))
print(canIWin(10, 40))
print(canIWin(10, 50))
print(canIWin(10, 60))
print(canIWin(10, 70))
print(canIWin(10, 80))
print(canIWin(10, 90))
print(canIWin(10, 100))
print(canIWin(10, 110))
print(canIWin(10, 120))
print(canIWin(10, 130))
print(canIWin(10, 140))
print(canIWin(10, 150))
print(canIWin(10, 160))
print(canIWin(10, 170))
print(canIWin(10, 180))
print(canIWin(10, 190))
print(canIWin(10, 200))
print(canIWin(10, 210))
print(canIWin(10, 220))
print(canI

=======
Suggestion 6

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
        return False
    memo = {}
    def helper(choices, desiredTotal):
        if choices[-1] >= desiredTotal:
            return True
        if str(choices) in memo:
            return memo[str(choices)]
        for i in range(len(choices)):
            if not helper(choices[:i] + choices[i+1:], desiredTotal - choices[i]):
                memo[str(choices)] = True
                return True
        memo[str(choices)] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(20, 300))
print(canIWin(20, 301))
print(canIWin(20, 302))
print(canIWin(20, 303))
print(canIWin(20, 304))
print(canIWin(20, 305))
print(canIWin(20, 306))
print(canIWin(20, 307))
print(canIWin(20, 308))
print(canIWin(20, 309))
print(canIWin(20, 310))
print(canIWin(20, 311))
print(canIWin(20, 312))
print(canIWin(20, 313))
print(canIWin(20, 314))
print(canIWin(20, 315))
print(canIWin(20, 316))
print(canIWin(20, 317))
print(canIWin(20, 318))
print(canIWin(20, 319))
print(canIWin(20, 320))
print(canIWin(20, 321))
print(canIWin(20, 322))
print(canIWin(20, 323))
print(canIWin(20, 324))
print(canIWin(20, 325))
print(canIWin(20, 326))
print(canIWin(20, 327))
print(canIWin(20, 328))
print(canIWin(20, 329))
print(canIWin

=======
Suggestion 7

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= 0:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) // 2 < desiredTotal:
        return False
    if maxChoosableInteger >= desiredTotal:
        return True
    if maxChoosableInteger == desiredTotal - 1:
        return False
    return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

=======
Suggestion 8

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger * (maxChoosableInteger + 1)) / 2 < desiredTotal:
        return False
    def helper(choices, desiredTotal):
        if choices[-1] >= desiredTotal:
            return True
        for i in range(len(choices)):
            if not helper(choices[:i] + choices[i + 1:], desiredTotal - choices[i]):
                return True
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 101))

=======
Suggestion 9

def canIWin(maxChoosableInteger, desiredTotal):
    pass

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
    if (maxChoosableInteger+1)*maxChoosableInteger//2 < desiredTotal:
        return False
    def helper(used, desiredTotal):
        if desiredTotal <= 0:
            return False
        key = tuple(used)
        if key in memo:
            return memo[key]
        for i in range(1, maxChoosableInteger+1):
            if used[i]:
                continue
            used[i] = True
            if not helper(used, desiredTotal-i):
                memo[key] = True
                used[i] = False
                return True
            used[i] = False
        memo[key] = False
        return False
    memo = {}
    used = [False]*(maxChoosableInteger+1)
    return helper(used, desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(20, 210))
print("The booleans above should be False, True, True, True, and False.")
