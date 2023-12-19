def integerReplacement(n):
    if n == 1:
        return 0
    if n % 2 == 0:
        return 1 + integerReplacement(n/2)
    else:
        return 1 + min(integerReplacement(n-1), integerReplacement(n+1))

if __name__ == '__main__':
    integerReplacement()