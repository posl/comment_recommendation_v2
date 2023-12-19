def canPartition(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #find the sum of the array
    total = sum(nums)
    #if the sum is odd, return false
    if total % 2 != 0:
        return False
    #if the sum is even, find the half of the sum
    half = int(total/2)
    #create a dp array with the size of half + 1
    dp = [False] * (half + 1)
    dp[0] = True
    #loop through the array
    for num in nums:
        #loop through the dp array from half to the number
        for i in range(half, num - 1, -1):
            #if the dp at i - num is true, set the dp at i to true
            if dp[i - num]:
                dp[i] = True
    #return the last element of the dp array
    return dp[-1]

if __name__ == '__main__':
    canPartition()