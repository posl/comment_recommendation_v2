def numberOfSteps (num):
    steps = 0
    while num != 1:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1
    return steps
print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
