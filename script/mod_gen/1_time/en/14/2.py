def integerBreak(n):
    if n == 2:
        return 1
    elif n == 3:
        return 2
    else:
        if n%3 == 0:
            return 3**(n//3)
        elif n%3 == 1:
            return 3**(n//3-1)*4
        else:
            return 3**(n//3)*2

if __name__ == '__main__':
    integerBreak()