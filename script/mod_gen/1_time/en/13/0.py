def numberOfSteps(num):
    """
    :type num: int
    :rtype: int
    """
    steps = 0
    while num > 0:
        if num % 2 == 0:
            num = num / 2
        else:
            num = num - 1
        steps += 1
    return steps

if __name__ == '__main__':
    num = ==========please modify============
    a = numberOfSteps(num)
    print(a)