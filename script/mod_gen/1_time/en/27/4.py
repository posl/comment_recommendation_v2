def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    count = 0
    for i in range(1, n+1):
        for j in str(i):
            if j == '1':
                count += 1
    return count

if __name__ == '__main__':
    n = int(input())
    a = countDigitOne(n)
    print(a)