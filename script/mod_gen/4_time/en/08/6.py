def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Brute Force
    #O(n^2)
    #O(1)
    max_val = -float("inf")
    for i in range(len(nums)):
        val = 0
        for j in range(len(nums)):
            val += j*nums[(j+i)%len(nums)]
        max_val = max(max_val, val)
    return max_val

if __name__ == '__main__':
    maxRotateFunction()