Synthesizing 10/10 solutions (Duplicates hidden)

=======
Suggestion 1

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False

    if len(stones) == 2:
        return True

    if stones[2] != 3:
        return False

    if len(stones) == 3:
        return True

    if stones[3] != 6:
        return False

    if len(stones) == 4:
        return True

    if stones[4] != 10:
        return False

    if len(stones) == 5:
        return True

    if stones[5] != 15:
        return False

    if len(stones) == 6:
        return True

    if stones[6] != 21:
        return False

    if len(stones) == 7:
        return True

    if stones[7] != 28:
        return False

    if len(stones) == 8:
        return True

    if stones[8] != 36:
        return False

    if len(stones) == 9:
        return True

    if stones[9] != 45:
        return False

    if len(stones) == 10:
        return True

    if stones[10] != 55:
        return False

    if len(stones) == 11:
        return True

    if stones[11] != 66:
        return False

    if len(stones) == 12:
        return True

    if stones[12] != 78:
        return False

    if len(stones) == 13:
        return True

    if stones[13] != 91:
        return False

    if len(stones) == 14:
        return True

    if stones[14] != 105:
        return False

    if len(stones) == 15:
        return True

    if stones[15] != 120:
        return False

    if len(stones) == 16:
        return True

    if stones[16] != 136:
        return False

    if len(stones) == 17:
        return True

    if stones[17] != 153:
        return False

    if len(stones) == 18:
        return True

=======
Suggestion 2

def canCross(stones):
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return stones[2] == 2
    if stones[2] > 3:
        return False
    if stones[-1] > stones[1] * 2:
        return False
    if stones[-1] == stones[1] * 2:
        return True
    if stones[-1] == stones[1] * 2 - 1:
        return True
    if stones[-1] == stones[1] * 2 + 1:
        return True
    if stones[-1] == stones[1] * 2 - 2:
        return True
    if stones[-1] == stones[1] * 2 + 2:
        return True
    if stones[-1] == stones[1] * 2 - 3:
        return True
    if stones[-1] == stones[1] * 2 + 3:
        return True
    if stones[-1] == stones[1] * 2 - 4:
        return True
    if stones[-1] == stones[1] * 2 + 4:
        return True
    if stones[-1] == stones[1] * 2 - 5:
        return True
    if stones[-1] == stones[1] * 2 + 5:
        return True
    if stones[-1] == stones[1] * 2 - 6:
        return True
    if stones[-1] == stones[1] * 2 + 6:
        return True
    if stones[-1] == stones[1] * 2 - 7:
        return True
    if stones[-1] == stones[1] * 2 + 7:
        return True
    if stones[-1] == stones[1] * 2 - 8:
        return True
    if stones[-1] == stones[1] * 2 + 8:
        return True
    if stones[-1] == stones[1] * 2 - 9:
        return True
    if stones[-1] == stones[1] * 2 + 9:
        return True

=======
Suggestion 3

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    stones_set = set(stones)
    def dp(position, jump):
        if position == stones[-1]:
            return True
        if position not in stones_set:
            return False
        return dp(position + jump + 1, jump + 1) or dp(position + jump, jump) or dp(position + jump - 1, jump - 1)
    return dp(1, 1)

print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))

=======
Suggestion 4

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if len(stones) == 0:
        return False
    if len(stones) == 1:
        return True
    if len(stones) == 2:
        if stones[1] == 1:
            return True
        else:
            return False
    if stones[1] != 1:
        return False
    
    i = 1
    while i < len(stones):
        if stones[i] - stones[i-1] > i:
            return False
        i += 1
    return True

=======
Suggestion 5

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        if stones[2] == 2:
            return True
        else:
            return False
    stones = stones[1:]
    last = stones[-1]
    stones = stones[:-1]
    setStones = set(stones)
    stones = [0] + stones
    #print(stones)
    #print(setStones)
    #print(last)
    def canJump(stone, jump):
        #print(stone, jump)
        if stone == last:
            return True
        if stone + jump + 1 in setStones:
            if canJump(stone + jump + 1, jump + 1):
                return True
        if stone + jump in setStones:
            if canJump(stone + jump, jump):
                return True
        if jump - 1 > 0 and stone + jump - 1 in setStones:
            if canJump(stone + jump - 1, jump - 1):
                return True
        return False
    return canJump(0, 1)

=======
Suggestion 6

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    if stones[1] != 1:
        return False
    steps = {x: set() for x in stones}
    steps[1].add(1)
    for i in range(1, len(stones)):
        for j in steps[stones[i]]:
            for k in range(j-1, j+2):
                if k > 0 and stones[i]+k in steps:
                    steps[stones[i]+k].add(k)
    return len(steps[stones[-1]]) > 0

=======
Suggestion 7

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    if stones[1] > 1:
        return False
    dp = {}
    for s in stones:
        dp[s] = set()
    dp[0].add(1)
    for s in stones:
        for step in dp[s]:
            if s + step in dp:
                dp[s + step].add(step)
                dp[s + step].add(step + 1)
                if step - 1 > 0:
                    dp[s + step].add(step - 1)
    return len(dp[stones[-1]]) > 0

print(canCross([0,1,3,5,6,8,12,17]))
print(canCross([0,1,2,3,4,8,9,11]))
print(canCross([0,2]))
print(canCross([0,1,3,6,10,15,16,21]))
print(canCross([0,1,3,6,9,10,13,15,18]))
print(canCross([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(canCross([0,1,3,4,5,7,9,10,12]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,25]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,27]))
print(canCross([0,1,3,4,5,7,9,10,12,13,14,15,16,17,18,19,20,21,22,23,24,27,28]))
print(canCross([0,1,3,4,5,7,9,10,12,

=======
Suggestion 8

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    #if stones[1] != 1:
    #    return False
    #if len(stones) == 2:
    #    return True
    #if len(stones) == 3:
    #    if stones[2] - stones[1] > 1:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 4:
    #    if stones[3] - stones[2] > 2:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 5:
    #    if stones[4] - stones[3] > 3:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 6:
    #    if stones[5] - stones[4] > 4:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 7:
    #    if stones[6] - stones[5] > 5:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 8:
    #    if stones[7] - stones[6] > 6:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 9:
    #    if stones[8] - stones[7] > 7:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 10:
    #    if stones[9] - stones[8] > 8:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 11:
    #    if stones[10] - stones[9] > 9:
    #        return False
    #    else:
    #        return True
    #if len(stones) == 12:
    #    if stones[11] - stones[10] > 10:
    #        return False
    #    else

=======
Suggestion 9

def canCross(stones):
    """
    :type stones: List[int]
    :rtype: bool
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    if stones[1] != 1:
        return False
    if len(stones) == 2:
        return True
    if len(stones) == 3:
        return True if stones[2] == 2 else False
    dp = {}
    for stone in stones:
        dp[stone] = set()
    dp[0].add(1)
    for stone in stones[:-1]:
        for step in dp[stone]:
            if stone + step == stones[-1]:
                return True
            if stone + step in dp:
                dp[stone + step].add(step)
                dp[stone + step].add(step + 1)
                dp[stone + step].add(step - 1)
    return False
