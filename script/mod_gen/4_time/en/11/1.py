def lengthOfLIS(nums):
    if len(nums) == 0:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)
print(lengthOfLIS([10,9,2,5,3,7,101,18]))
print(lengthOfLIS([0,1,0,3,2,3]))
print(lengthOfLIS([7,7,7,7,7,7,7]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,20,30,40,50,60,70,80,90,100,110]))
print(lengthOfLIS([1,3,6,7,9,4,10,5,6,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200]))
