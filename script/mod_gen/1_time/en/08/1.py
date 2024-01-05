def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    sumNums = sum(nums)
    F = 0
    n = len(nums)
    for i in range(n):
        F += i*nums[i]
    maxF = F
    for i in range(1,n):
        F = F + sumNums - n*nums[n-i]
        maxF = max(maxF, F)
    return maxF

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = maxRotateFunction(nums)
    print(a)