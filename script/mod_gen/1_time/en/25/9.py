def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    if len(nums) == 2:
        return max(nums[0]*nums[1]+nums[1], nums[0]*nums[1]+nums[0])
    if len(nums) == 3:
        return max(nums[0]*nums[1]*nums[2]+nums[0]*nums[2]+nums[1], nums[0]*nums[1]*nums[2]+nums[0]*nums[1]+nums[2], nums[0]*nums[1]*nums[2]+nums[1]*nums[2]+nums[0])
    else:
        max_coins = 0
        for i in range(len(nums)):
            if i == 0:
                max_coins = max(max_coins, nums[i]*nums[i+1]*nums[i+2]+maxCoins(nums[i+2:]))
            elif i == len(nums)-1:
                max_coins = max(max_coins, nums[i-1]*nums[i]*nums[i+1]+maxCoins(nums[:i-1]))
            else:
                max_coins = max(max_coins, nums[i-1]*nums[i]*nums[i+1]+maxCoins(nums[:i-1]+nums[i+2:]))
        return max_coins
print(maxCoins([3,1,5,8]))
print(maxCoins([
