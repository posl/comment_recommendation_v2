def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    max_sum = float('-inf')
    for i in range(len(nums)):
        sum = 0
        for j in range(len(nums)):
            sum += j * nums[(j + i) % len(nums)]
        max_sum = max(max_sum, sum)
    return max_sum

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = maxRotateFunction(nums)
    print(a)