def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n)
    if len(nums) == 0:
        return []
    nums.sort()
    dp = [1] * len(nums)
    prev = [-1] * len(nums)
    max_dp = 1
    max_index = 0
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev[i] = j
        if dp[i] > max_dp:
            max_dp = dp[i]
            max_index = i
    ans = []
    while max_index != -1:
        ans.append(nums[max_index])
        max_index = prev[max_index]
    return ans[::-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = largestDivisibleSubset(nums)
    print(a)