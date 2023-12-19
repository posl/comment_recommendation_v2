def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count
print(countDigitOne(13))
print(countDigitOne(0))
print(countDigitOne(1))
