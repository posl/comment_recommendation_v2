def largestDivisibleSubset(nums):
    nums.sort()
    dp = [1] * len(nums)
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j]+1)
    maxIndex = dp.index(max(dp))
    ans = []
    prev = nums[maxIndex]
    for i in range(maxIndex, -1, -1):
        if prev % nums[i] == 0 and dp[i] == dp[maxIndex]:
            ans.append(nums[i])
            prev = nums[i]
            maxIndex -= 1
    return ans[::-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = largestDivisibleSubset(nums)
    print(a)