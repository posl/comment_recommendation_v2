def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7]))
print(lengthOfLIS([0,1,0,3,2,3,4,5,6,7,8,9,10,1,2,3,4,5,6,7,8]))
print(length

if __name__ == '__main__':
    lengthOfLIS()