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

if __name__ == '__main__':
    canIWin()