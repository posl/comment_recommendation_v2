def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    result = []
    for i in range(num+1):
        result.append(bin(i).count('1'))
    return result
print(countBits(5))
