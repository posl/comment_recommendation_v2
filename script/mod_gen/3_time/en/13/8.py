def min_steps(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            if n == 3:
                count += 2
                break
            if (n + 1) % 4 == 0:
                n += 1
            else:
                n -= 1
        count += 1
    return count
n = 8
print(min_steps(n))
n = 7
print(min_steps(n))
n = 4
print(min_steps(n))
