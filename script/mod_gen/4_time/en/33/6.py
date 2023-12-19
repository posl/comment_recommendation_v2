def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #Solution 1
    #The idea is to use a 2D array dp[i][j] to record the number of arithmetic slices ending with nums[i] and the common difference is j.
    #For each i, we iterate all the previous elements to see if they can form arithmetic slices with nums[i] and update the dp array.
    #Time complexity: O(n^2)
    #Space complexity: O(n^2)
    n = len(nums)
    dp = [{} for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + dp[i].get(diff, 0) + 1
            else:
                dp[i][diff] = dp[i].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res
    #Solution 2
    #The idea is to use a 2D array dp[i][j] to record the number of arithmetic slices ending with nums[i] and the common difference is j.
    #For each i, we iterate all the previous elements to see if they can form arithmetic slices with nums[i] and update the dp array.
    #Time complexity: O(n^2)
    #Space complexity: O(n^2)
    n = len(nums)
    dp = [{} for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res
    #Solution 3
    #The idea is to use a 2D array dp[i][j] to record the number of arithmetic slices ending with nums[i] and the common difference is j.
    #For each i, we iterate all the previous elements to see if they can form arithmetic slices with nums[i] and update the dp array.
    #Time complexity: O(n

if __name__ == '__main__':
    numberOfArithmeticSlices()