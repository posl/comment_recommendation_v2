def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    dp = [{} for i in nums]
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            count += dp[j].get(diff, 0)
    return count
print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
print(numberOfArithmeticSlices([1,1,1,1,1,1,1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(number

if __name__ == '__main__':
    numberOfArithmeticSlices()