def number_of_steps(n):
    steps = 0
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n = n - 1
            steps += 1
    return steps
print(number_of_steps(8))
print(number_of_steps(7))
print(number_of_steps(4))
print(number_of_steps(123))
print(number_of_steps(123456789))
print(number_of_steps(1234567890))
print(number_of_steps(12345678901))
print(number_of_steps(123456789012))
print(number_of_steps(1234567890123))
print(number_of_steps(12345678901234))
print(number_of_steps(123456789012345))
print(number_of_steps(1234567890123456))
print(number_of_steps(12345678901234567))
print(number_of_steps(123456789012345678))
print(number_of_steps(1234567890123456789))
print(number_of_steps(12345678901234567890))
print(number_of_steps(123456789012345678901))
print(number_of_steps(1234567890123456789012))
print(number_of_steps(12345678901234567890123))
print(number_of_steps(123456789012345678901234))
print(number_of_steps(1234567890123456789012345))
print(number_of_steps(12345678901234567890123456))
print(number_of_steps(123456789012345678901234567))
print(number_of_steps(1234567890123456789012345678))
print(number_of_steps(12345678901234567890123456789))
print(number_of_steps(123456789012345678901234567890))
print(number_of_steps(1234567890123456789012345678901))
print(number_of_steps(12345678901234567890123456789012))
print(number_of_steps(123456789012345678901234567890123))
print(number_of_steps(1234567890123456789012345678901234))
print(number_of_steps(12345678901234567890123456789012345))
print(number_of_steps(123456789012345678901234567890123456))
print(number_of_steps(1234567890123456789012345678901234567))
print(number_of

if __name__ == '__main__':
    number_of_steps()