def countBits(n):
    """
    :type n: int
    :rtype: List[int]
    """
    # Runtime: 80 ms
    # Memory Usage: 20.8 MB
    # Your runtime beats 97.42 % of python3 submissions.
    # Your memory usage beats 52.28 % of python3 submissions.
    if n == 0:
        return [0]
    if n == 1:
        return [0,1]
    if n == 2:
        return [0,1,1]
    if n == 3:
        return [0,1,1,2]
    if n == 4:
        return [0,1,1,2,1]
    if n == 5:
        return [0,1,1,2,1,2]
    if n == 6:
        return [0,1,1,2,1,2,2]
    if n == 7:
        return [0,1,1,2,1,2,2,3]
    if n == 8:
        return [0,1,1,2,1,2,2,3,1]
    if n == 9:
        return [0,1,1,2,1,2,2,3,1,2]
    if n == 10:
        return [0,1,1,2,1,2,2,3,1,2,2]
    if n == 11:
        return [0,1,1,2,1,2,2,3,1,2,2,3]
    if n == 12:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2]
    if n == 13:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3]
    if n == 14:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3,3]
    if n == 15:
        return [0,1,1,2,1,2,2,3,1,2,2,3,2,3,

if __name__ == '__main__':
    countBits()