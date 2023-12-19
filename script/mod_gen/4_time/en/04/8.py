def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    result = []
    for i in range(n+1):
        num = i
        count = 0
        while num:
            count += num & 1
            num >>= 1
        result.append(count)
    return result

if __name__ == '__main__':
    countBits()