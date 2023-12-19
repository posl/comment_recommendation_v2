def number_of_steps(n):
    count = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n - 1
        count += 1
    return count
print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
