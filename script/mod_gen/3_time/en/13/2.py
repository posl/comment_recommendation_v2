def numberOfSteps(num):
    step = 0
    while(num > 0):
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        step += 1
    return step
print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
print(numberOfSteps(123))
print(numberOfSteps(123456789))
print(numberOfSteps(987654321))
print(numberOfSteps(1234567890))
print(numberOfSteps(12345678901))
print(numberOfSteps(123456789012))
print(numberOfSteps(1234567890123))
print(numberOfSteps(12345678901234))
print(numberOfSteps(123456789012345))
print(numberOfSteps(1234567890123456))
print(numberOfSteps(12345678901234567))
print(numberOfSteps(123456789012345678))
print(numberOfSteps(1234567890123456789))
print(numberOfSteps(12345678901234567890))
print(numberOfSteps(123456789012345678901))
print(numberOfSteps(1234567890123456789012))
print(numberOfSteps(12345678901234567890123))
print(numberOfSteps(123456789012345678901234))
print(numberOfSteps(1234567890123456789012345))
print(numberOfSteps(12345678901234567890123456))
print(numberOfSteps(123456789012345678901234567))
print(numberOfSteps(1234567890123456789012345678))
print(numberOfSteps(12345678901234567890123456789))
print(numberOfSteps(123456789012345678901234567890))
print(numberOfSteps(1234567890123456789012345678901))
print(numberOfSteps(12345678901234567890123456789012))
print(numberOfSteps(123456789012345678901234567890123))
print(numberOfSteps(1234567890123456789012345678901234))
print(numberOfSteps(12345678901234567890123456789012345))
print(numberOfSteps(123456789012345678901234567890123456))
print(numberOfSteps(1234567890123456789012345678901234567))
print

if __name__ == '__main__':
    numberOfSteps()