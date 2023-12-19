def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    maxVal = 0
    for i in range(len(nums)):
        maxVal += i * nums[i]
    sumVal = maxVal
    for i in range(len(nums)-1,0,-1):
        sumVal += sum(nums) - len(nums) * nums[i]
        maxVal = max(maxVal, sumVal)
    return maxVal
print(maxRotateFunction([4,3,2,6])) #26
print(maxRotateFunction([100])) #0
print(maxRotateFunction([1,2,3,4,5,6,7,8,9,10])) #330
print(maxRotateFunction([-2147483648,-2147483648])) #0
print(maxRotateFunction([2147483647,2147483647])) #0
print(maxRotateFunction([2147483647,-2147483648])) #0
print(maxRotateFunction([2147483647,-2147483648,2147483647])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647,-2147483648])) #2147483647
print(maxRotateFunction([2147483647,-2147483648,2147483647,-2147483648,2147483647,-2147483648,2147483647])) #2147483647
print

if __name__ == '__main__':
    maxRotateFunction()