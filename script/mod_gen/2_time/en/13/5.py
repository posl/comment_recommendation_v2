def minOperations(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n -= 1
        count += 1
    return count
print(minOperations(8))
print(minOperations(7))
print(minOperations(4))
