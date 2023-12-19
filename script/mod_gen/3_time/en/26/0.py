def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # 1. find the min and max of the array
    # 2. use binary search to find the min max sum
    # 3. check if the sum is valid
    # 4. return the min max sum
    # 5. check if the sum is valid
    # 6. return the min max sum
    if len(nums) == 0:
        return 0
    if len(nums) == 1:
        return nums[0]
    minSum = max(nums)
    maxSum = sum(nums)
    def isValid(mid):
        count = 1
        currSum = 0
        for num in nums:
            currSum += num
            if currSum > mid:
                count += 1
                currSum = num
                if count > m:
                    return False
        return True
    while minSum < maxSum:
        mid = (minSum + maxSum) // 2
        if isValid(mid):
            maxSum = mid
        else:
            minSum = mid + 1
    return minSum
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print(splitArray([2,3,1,2,4,3], 5))
print(splitArray([1,2147483647], 2))
print("The values above should be 18, 9, 4, 4, and 2147483647.")

if __name__ == '__main__':
    splitArray()