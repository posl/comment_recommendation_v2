def problem13(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            if (n + 1) % 4 == 0 and n != 3:
                n = n + 1
            else:
                n = n - 1
        count += 1
    return count
print(problem13(8))
print(problem13(7))
print(problem13(4))
