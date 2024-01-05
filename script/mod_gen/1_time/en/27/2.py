def countDigitOne(n):
    res = 0
    for i in range(1, n+1):
        res += str(i).count('1')
    return res

if __name__ == '__main__':
    n = int(input())
    a = countDigitOne(n)
    print(a)