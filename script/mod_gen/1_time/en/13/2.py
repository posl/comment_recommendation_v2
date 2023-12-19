def numberOfSteps(n):
    count = 0
    while n > 0:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count
print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
