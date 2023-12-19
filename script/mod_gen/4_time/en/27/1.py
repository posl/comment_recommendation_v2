def countDigitOne(n):
    """
    :type n: int
    :rtype: int
    """
    if n < 1:
        return 0
    if n < 10:
        return 1
    if n < 20:
        return 2
    if n < 100:
        return n//10 + 10 + countDigitOne(n%10)
    if n < 200:
        return n//100 + 20 + countDigitOne(n%100)
    if n < 1000:
        return n//100 + 10*countDigitOne(n%100)
    if n < 2000:
        return n//1000 + 100 + countDigitOne(n%1000)
    if n < 10000:
        return n//1000 + 10*countDigitOne(n%1000)
    if n < 20000:
        return n//10000 + 1000 + countDigitOne(n%10000)
    if n < 100000:
        return n//10000 + 10*countDigitOne(n%10000)
    if n < 200000:
        return n//100000 + 10000 + countDigitOne(n%100000)
    if n < 1000000:
        return n//100000 + 10*countDigitOne(n%100000)
    if n < 2000000:
        return n//1000000 + 100000 + countDigitOne(n%1000000)
    if n < 10000000:
        return n//1000000 + 10*countDigitOne(n%1000000)
    if n < 20000000:
        return n//10000000 + 1000000 + countDigitOne(n%10000000)
    if n < 100000000:
        return n//10000000 + 10*countDigitOne(n%10000000)
    if n < 200000000:
        return n//100000000 + 10000000 + countDigitOne(n%100000000)
    if n < 1000000000:
        return n//100000000 + 10*countDigitOne(n%100000000)
    if n < 2000000000:
        return n//1000000000 + 100000000 + countDigitOne(n%1000000000

if __name__ == '__main__':
    countDigitOne()