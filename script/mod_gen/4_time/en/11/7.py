def lengthOfLIS(nums):
    n = len(nums)
    lis = [1]*n
    for i in range(1,n):
        for j in range(i):
            if nums[i]>nums[j] and lis[i]<lis[j]+1:
                lis[i] = lis[j]+1
    return max(lis)
nums = [10,9,2,5,3,7,101,18]
print(lengthOfLIS(nums))
