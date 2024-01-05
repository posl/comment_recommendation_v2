def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n<=0:
        return 0
    if n<10:
        return 1
    if n<100:
        return 20
    if n<1000:
        return 300
    if n<10000:
        return 4000
    if n<100000:
        return 50000
    if n<1000000:
        return 600000
    if n<10000000:
        return 7000000
    if n<100000000:
        return 80000000
    if n<1000000000:
        return 900000000
    if n==1000000000:
        return 1000000000
    return 0

if __name__ == '__main__':
    n = int(input())
    a = countDigitOne(n)
    print(a)