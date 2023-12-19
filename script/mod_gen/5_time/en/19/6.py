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

if __name__ == '__main__':
    canIWin()