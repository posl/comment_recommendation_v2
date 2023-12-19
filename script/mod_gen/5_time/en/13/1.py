def reduceNumber(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n/2
            count += 1
        else:
            n = n - 1
            count += 1
    return count
print(reduceNumber(8))
print(reduceNumber(7))
print(reduceNumber(4))
