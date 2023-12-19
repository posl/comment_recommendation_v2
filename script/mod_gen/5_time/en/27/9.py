def countDigitOne(n):
    total = 0
    for i in range(1, n+1):
        total += str(i).count('1')
    return total
print(countDigitOne(13))
print(countDigitOne(0))
