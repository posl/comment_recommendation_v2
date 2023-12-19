def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    F = [0] * len(nums)
    for i in range(len(nums)):
        for j in range(len(nums)):
            F[i] += j * nums[(j - i) % len(nums)]
    return max(F)

if __name__ == '__main__':
    maxRotateFunction()