def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        count += str(i).count('1')
    return count
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1000))
