def number_of_steps(num):
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        steps += 1
    return steps
print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
print(number_of_steps(123))
print(number_of_steps(0))
print(number_of_steps(1))
print(number_of_steps(2**31-1))
