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

if __name__ == '__main__':
    canIWin()