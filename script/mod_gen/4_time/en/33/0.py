def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp = [collections.defaultdict(int) for _ in range(len(nums))]
    dp = [{} for _ in range(len(nums))]
    res = 0
    for i in range(len(nums)):
        for j in range(i):
            d = nums[i] - nums[j]
            c1 = dp[i].get(d, 0)
            c2 = dp[j].get(d, 0)
            res += c2
            dp[i][d] = c1 + c2 + 1
    return res

if __name__ == '__main__':
    numberOfArithmeticSlices()