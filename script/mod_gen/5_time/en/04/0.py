def countBits(n):
    result = []
    for i in range(n+1):
        result.append(bin(i).count('1'))
    return result
print(countBits(5))
