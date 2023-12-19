def countDigitOne(n):
    count = 0
    for i in range(1,n+1):
        for j in str(i):
            if j == '1':
                count+=1
    return count
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
print(countDigitOne(10))
print(countDigitOne(11))
print(countDigitOne(12))
print(countDigitOne(100))
print(countDigitOne(101))
print(countDigitOne(102))
print(countDigitOne(111))
