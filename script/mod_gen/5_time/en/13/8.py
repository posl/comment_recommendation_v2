def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    count = 0
    while num != 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        count = count + 1
    return count
print(numberOfSteps(8))
print(numberOfSteps(7))
print(numberOfSteps(4))
