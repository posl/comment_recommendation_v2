def countBits(num):
    """
    :type num: int
    :rtype: List[int]
    """
    ans = []
    for i in range(num + 1):
        ans.append(bin(i).count('1'))
    return ans
print(countBits(5))
