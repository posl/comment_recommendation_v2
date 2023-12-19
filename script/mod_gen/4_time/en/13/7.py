def reduceToOne(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n -= 1
        count += 1
    return count
print(reduceToOne(8))
print(reduceToOne(7))
print(reduceToOne(4))
