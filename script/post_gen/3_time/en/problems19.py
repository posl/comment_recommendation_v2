Synthesizing 10/10 solutions

=======
Suggestion 1

def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return canIWinHelper(range(1, maxChoosableInteger + 1), desiredTotal)

=======
Suggestion 2

def canIWin(maxChoosableInteger: int, desiredTotal: int) -> bool:
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    return canIWinHelper(maxChoosableInteger, desiredTotal, 0, {})

=======
Suggestion 3

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    elif sum(range(maxChoosableInteger+1)) < desiredTotal:
        return False
    else:
        return True if desiredTotal % (maxChoosableInteger+1) != 0 else False

print(canIWin(10,11))
print(canIWin(10,0))
print(canIWin(10,1))
print(canIWin(10,2))
print(canIWin(10,3))
print(canIWin(10,4))
print(canIWin(10,5))
print(canIWin(10,6))
print(canIWin(10,7))
print(canIWin(10,8))
print(canIWin(10,9))
print(canIWin(10,10))
print(canIWin(10,11))
print(canIWin(10,12))
print(canIWin(10,13))
print(canIWin(10,14))
print(canIWin(10,15))
print(canIWin(10,16))
print(canIWin(10,17))
print(canIWin(10,18))
print(canIWin(10,19))
print(canIWin(10,20))
print(canIWin(10,21))
print(canIWin(10,22))
print(canIWin(10,23))
print(canIWin(10,24))
print(canIWin(10,25))
print(canIWin(10,26))
print(canIWin(10,27))
print(canIWin(10,28))
print(canIWin(10,29))
print(canIWin(10,30))
print(canIWin(10,31))
print(canIWin(10,32))
print(canIWin(10,33))
print(canIWin(10,34))
print(canIWin(10,35))
print(canIWin(10,36))
print(canIWin(10,37))
print(canIWin(10,38))
print(canIWin(10,39))
print(canIWin(10,40))
print(canIWin(10,41))
print(canIWin(10,42))
print(canIWin(10,43))
print(canIWin(10,44))
print(canIWin(10,45))
print(canIWin(

=======
Suggestion 4

def canIWin(maxChoosableInteger, desiredTotal):
    #if total is less than 1, return true
    if desiredTotal <= 0:
        return True
    #if total is more than sum of all integers, return false
    if (maxChoosableInteger*(maxChoosableInteger+1)/2) < desiredTotal:
        return False
    #if total is equal to sum of all integers, return true if maxChoosableInteger is even, else false
    if (maxChoosableInteger*(maxChoosableInteger+1)/2) == desiredTotal:
        return maxChoosableInteger%2 == 0
    #if total is less than 2*maxChoosableInteger, return true
    if 2*maxChoosableInteger < desiredTotal:
        return True
    #if total is equal to 2*maxChoosableInteger, return true if maxChoosableInteger is odd, else false
    if 2*maxChoosableInteger == desiredTotal:
        return maxChoosableInteger%2 != 0
    #if total is between 2*maxChoosableInteger and sum of all integers, return true
    if 2*maxChoosableInteger < desiredTotal < (maxChoosableInteger*(maxChoosableInteger+1)/2):
        return True
    #if total is equal to sum of all integers, return true if maxChoosableInteger is even, else false
    if (maxChoosableInteger*(maxChoosableInteger+1)/2) == desiredTotal:
        return maxChoosableInteger%2 == 0
    #if total is equal to sum of all integers, return true if maxChoosableInteger is even, else false
    if (maxChoosableInteger*(maxChoosableInteger+1)/2) == desiredTotal:
        return maxChoosableInteger%2 == 0
    #if total is equal to sum of all integers, return true if maxChoosableInteger is even, else false
    if (maxChoosableInteger*(maxChoosableInteger+1)/2) == desiredTotal:
        return maxChoosableInteger%2 == 0
    #if total is equal to sum of all integers, return true if maxChoosableInteger is

=======
Suggestion 5

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1 + maxChoosableInteger) * maxChoosableInteger / 2 < desiredTotal:
        return False
    def canIWinHelper(nums, desiredTotal, cache):
        if nums[-1] >= desiredTotal:
            return True
        key = tuple(nums)
        if key in cache:
            return cache[key]
        for i in range(len(nums)):
            if not canIWinHelper(nums[:i] + nums[i + 1:], desiredTotal - nums[i], cache):
                cache[key] = True
                return True
        cache[key] = False
        return False
    return canIWinHelper(list(range(1, maxChoosableInteger + 1)), desiredTotal, {})

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 50))
print(canIWin(10, 100))
print(canIWin(10, 150))
print(canIWin(10, 200))
print(canIWin(10, 250))
print(canIWin(10, 300))
print(canIWin(10, 350))
print(canIWin(10, 400))
print(canIWin(10, 450))
print(canIWin(10, 500))
print(canIWin(10, 550))
print(canIWin(10, 600))
print(canIWin(10, 650))
print(canIWin(10, 700))
print(canIWin(10, 750))
print(canIWin(10, 800))
print(canIWin(10, 850))
print(canIWin(10, 900))
print(canIWin(10, 950))
print(canIWin(10, 1000))
print(canIWin(10, 1050))
print(canIWin(10, 1100))
print(canIWin(10, 1150))
print(canIWin(10, 1200))
print(canIWin(10, 1250))
print(canIWin(10, 1300))
print(canIWin(10, 1350))
print(can

=======
Suggestion 6

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger*(maxChoosableInteger+1))//2 < desiredTotal:
        return False
    memo = {}
    def helper(maxChoosableInteger, desiredTotal, used):
        if used in memo:
            return memo[used]
        for i in range(1, maxChoosableInteger+1):
            if used & (1 << i) == 0:
                if desiredTotal <= i or not helper(maxChoosableInteger, desiredTotal-i, used | (1 << i)):
                    memo[used] = True
                    return True
        memo[used] = False
        return False
    return helper(maxChoosableInteger, desiredTotal, 0)

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
print(can

=======
Suggestion 7

def canIWin(maxChoosableInteger, desiredTotal):
    """
    :type maxChoosableInteger: int
    :type desiredTotal: int
    :rtype: bool
    """
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    if maxChoosableInteger == 1:
        return desiredTotal == 1
    if maxChoosableInteger == 2:
        return desiredTotal % 2 == 0
    if maxChoosableInteger == 3:
        return desiredTotal % 3 != 0
    return canIWin(maxChoosableInteger - 3, desiredTotal - 3) or canIWin(maxChoosableInteger - 2, desiredTotal - 2) or canIWin(maxChoosableInteger - 1, desiredTotal - 1)

=======
Suggestion 8

def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal <= maxChoosableInteger:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    memo = {}
    def dfs(used, desiredTotal):
        if desiredTotal <= 0:
            return False
        if used in memo:
            return memo[used]
        for i in range(maxChoosableInteger):
            if used & (1 << i) == 0:
                if not dfs(used | (1 << i), desiredTotal - i - 1):
                    memo[used] = True
                    return True
        memo[used] = False
        return False
    return dfs(0, desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 100))
print(canIWin(10, 200))
print(canIWin(10, 300))
print(canIWin(10, 301))
print(canIWin(20, 210))
print(canIWin(20, 211))
print(canIWin(20, 220))
print(canIWin(20, 230))
print(canIWin(20, 240))
print(canIWin(20, 250))
print(canIWin(20, 260))
print(canIWin(20, 270))
print(canIWin(20, 280))
print(canIWin(20, 290))
print(canIWin(20, 300))
print(canIWin(20, 301))

=======
Suggestion 9

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (1+maxChoosableInteger)*maxChoosableInteger/2 < desiredTotal:
        return False
    def helper(nums, desiredTotal, memo):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not helper(nums[:i]+nums[i+1:], desiredTotal-nums[i], memo):
                memo[key] = True
                return True
        memo[key] = False
        return False
    memo = {}
    return helper(list(range(1, maxChoosableInteger+1)), desiredTotal, memo)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(18, 79))
print(canIWin(20, 209))
print(canIWin(20, 210))
print(canIWin(19, 190))
print(canIWin(19, 191))
print(canIWin(19, 192))
print(canIWin(19, 193))
print(canIWin(19, 194))
print(canIWin(19, 195))
print(canIWin(19, 196))
print(canIWin(19, 197))
print(canIWin(19, 198))
print(canIWin(19, 199))
print(canIWin(19, 200))
print(canIWin(19, 201))
print(canIWin(19, 202))
print(canIWin(19, 203))
print(canIWin(19, 204))
print(canIWin(19, 205))
print(canIWin(19, 206))
print(canIWin(19, 207))
print(canIWin(19, 208))
print(canIWin(19, 209))
print(canIWin(19, 210))
print(canIWin(19, 211))
print(canIWin(19, 212))
print(canIWin(19, 213))
print(canIWin(19, 214))
print(canIWin(19, 215))
print(canIWin(19, 216))

=======
Suggestion 10

def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if (maxChoosableInteger + 1) * maxChoosableInteger / 2 < desiredTotal:
        return False
    memo = {}
    def helper(nums, desiredTotal):
        if nums[-1] >= desiredTotal:
            return True
        key = str(nums)
        if key in memo:
            return memo[key]
        for i in range(len(nums)):
            if not helper(nums[:i] + nums[i+1:], desiredTotal - nums[i]):
                memo[key] = True
                return True
        memo[key] = False
        return False
    return helper(list(range(1, maxChoosableInteger + 1)), desiredTotal)

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 1))
print(canIWin(10, 40))
print(canIWin(10, 55))
print(canIWin(10, 56))
print(canIWin(10, 57))
print(canIWin(10, 58))
print(canIWin(10, 59))
print(canIWin(10, 60))
print(canIWin(10, 61))
print(canIWin(10, 62))
print(canIWin(10, 63))
print(canIWin(10, 64))
print(canIWin(10, 65))
print(canIWin(10, 66))
print(canIWin(10, 67))
print(canIWin(10, 68))
print(canIWin(10, 69))
print(canIWin(10, 70))
print(canIWin(10, 71))
print(canIWin(10, 72))
print(canIWin(10, 73))
print(canIWin(10, 74))
print(canIWin(10, 75))
print(canIWin(10, 76))
print(canIWin(10, 77))
print(canIWin(10, 78))
print(canIWin(10, 79))
print(canIWin(10, 80))
print(canIWin(10, 81))
print(canIWin(10, 82))
print(canIWin(10, 83))
print
