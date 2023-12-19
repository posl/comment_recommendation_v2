def numberOfSteps (num):
    count = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count = count + 1
    return count
print(numberOfSteps(8)) #3
print(numberOfSteps(7)) #4
print(numberOfSteps(4)) #2
