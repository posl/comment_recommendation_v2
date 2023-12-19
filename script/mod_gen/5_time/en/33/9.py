def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    # dp[i][j] stores the number of arithmetic slices ending at index i with difference j
    dp = [{} for _ in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,1,1,1,1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([7,3,5,1,9]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37]))
print(numberOfArithmeticSlices([1,3,5,7,
