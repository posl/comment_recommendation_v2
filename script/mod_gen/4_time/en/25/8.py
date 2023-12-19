def maxCoins(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return nums[0]
    elif len(nums) == 2:
        return max(nums[0]*nums[1] + nums[1], nums[0] + nums[1]*nums[0])
    else:
        max_coins = 0
        for i in range(len(nums)):
            if i == 0:
                max_coins = max_coins + nums[i]*nums[i+1] + maxCoins(nums[i+1:])
            elif i == len(nums)-1:
                max_coins = max_coins + nums[i-1]*nums[i] + maxCoins(nums[:i])
            else:
                max_coins = max_coins + nums[i-1]*nums[i]*nums[i+1] + maxCoins(nums[:i] + nums[i+1:])
    return max_coins
print(maxCoins([3,1,5,8]))
print(maxCoins([1,5]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(maxCoins([1,2,3,4,5,6,7,8,9,10,11,12,13
