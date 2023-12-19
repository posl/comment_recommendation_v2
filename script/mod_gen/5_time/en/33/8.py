def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [{} for _ in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[i]:
                dp[i][diff] += 1
            else:
                dp[i][diff] = 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                res += dp[j][diff]
    return res
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print("The values above should be 7, 16, and 10.")

if __name__ == '__main__':
    numberOfArithmeticSlices()