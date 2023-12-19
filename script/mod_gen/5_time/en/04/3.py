def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    answer = []
    for i in range(n+1):
        answer.append(bin(i)[2:].count('1'))
    return answer

if __name__ == '__main__':
    countBits()