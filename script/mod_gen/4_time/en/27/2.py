def countDigitOne(n):
    count = 0
    for i in range(n+1):
        count += str(i).count('1')
    return count
n = 13
print(countDigitOne(n))
n = 0
print(countDigitOne(n))
