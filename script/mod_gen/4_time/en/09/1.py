def canPartition(nums):
    if sum(nums) % 2 != 0:
        return False
    else:
        target = sum(nums) // 2
        dp = [[False for i in range(target+1)] for j in range(len(nums)+1)]
        for i in range(len(dp)):
            dp[i][0] = True
        for i in range(1,len(dp)):
            for j in range(1,len(dp[0])):
                if nums[i-1] <= j:
                    dp[i][j] = dp[i-1][j-nums[i-1]] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
print(canPartition([1,5,11,5]))
print(canPartition([1,2,3,5]))
print(canPartition([1,2,3,4,5,6,7]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,12]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,13]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,14]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,15]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,16]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,17]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,18]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,19]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,20]))
print(canPartition([1,2,3,4,5,6,7,8,9,10,11,21]))
print(canPartition([1,2,3,4,5,6,7,8,9,
