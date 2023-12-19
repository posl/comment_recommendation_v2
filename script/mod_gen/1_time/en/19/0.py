def canIWin(maxChoosableInteger, desiredTotal):
    if maxChoosableInteger >= desiredTotal:
        return True
    if sum(range(1,maxChoosableInteger+1)) < desiredTotal:
        return False
    if maxChoosableInteger == 1:
        return True
    if maxChoosableInteger == 2:
        return desiredTotal%2 == 0
    if maxChoosableInteger == 3:
        return desiredTotal%3 != 0
    if maxChoosableInteger == 4:
        return desiredTotal%4 != 0
    if maxChoosableInteger == 5:
        return desiredTotal%5 != 0
    if maxChoosableInteger == 6:
        return desiredTotal%6 != 0
    if maxChoosableInteger == 7:
        return desiredTotal%7 != 0
    if maxChoosableInteger == 8:
        return desiredTotal%8 != 0
    if maxChoosableInteger == 9:
        return desiredTotal%9 != 0
    if maxChoosableInteger == 10:
        return desiredTotal%10 != 0
    if maxChoosableInteger == 11:
        return desiredTotal%11 != 0
    if maxChoosableInteger == 12:
        return desiredTotal%12 != 0
    if maxChoosableInteger == 13:
        return desiredTotal%13 != 0
    if maxChoosableInteger == 14:
        return desiredTotal%14 != 0
    if maxChoosableInteger == 15:
        return desiredTotal%15 != 0
    if maxChoosableInteger == 16:
        return desiredTotal%16 != 0
    if maxChoosableInteger == 17:
        return desiredTotal%17 != 0
    if maxChoosableInteger == 18:
        return desiredTotal%18 != 0
    if maxChoosableInteger == 19:
        return desiredTotal%19 != 0
    if maxChoosableInteger == 20:
        return desiredTotal%20 != 0
print(canIWin(10,11))
print(canIWin(10,0))
print(canIWin(10,1))
print(canIWin(10,2))
print

if __name__ == '__main__':
    canIWin()