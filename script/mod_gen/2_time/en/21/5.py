def arithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1st approach
    # DP solution
    # Time complexity: O(n)
    # Space complexity: O(n)
    # dp = [0] * len(nums)
    # for i in range(2, len(nums)):
    #     if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
    #         dp[i] = dp[i-1] + 1
    # return sum(dp)
    # 2nd approach
    # Time complexity: O(n)
    # Space complexity: O(1)
    count = 0
    curr = 0
    for i in range(2, len(nums)):
        if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
            curr += 1
            count += curr
        else:
            curr = 0
    return count

if __name__ == '__main__':
    arithmeticSlices()