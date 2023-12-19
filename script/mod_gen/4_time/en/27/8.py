def countDigitOne(n):
    count = 0
    for i in range(1, n+1):
        for j in str(i):
            if j == '1':
                count += 1
    return count
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(100))
print(countDigitOne(1000))
print(countDigitOne(10000))
print(countDigitOne(100000))
print(countDigitOne(1000000))
print(countDigitOne(10000000))
print(countDigitOne(100000000))
print(countDigitOne(1000000000))
