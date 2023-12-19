def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    return [bin(i).count('1') for i in range(n+1)]
print(countBits(5))
print(countBits(2))
print(countBits(0))
print(countBits(10))
print("The arrays above should be [0, 1, 1, 2, 1, 2], \
    [0, 1, 1], [0], and [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2].")

if __name__ == '__main__':
    countBits()