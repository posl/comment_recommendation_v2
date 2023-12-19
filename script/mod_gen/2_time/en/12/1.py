def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    if len(nums) == 1:
        return nums
    nums.sort()
    res = [[num] for num in nums]
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[j]%nums[i] == 0 and len(res[i]) + 1 > len(res[j]):
                res[j] = res[i] + [nums[j]]
    return max(res, key=len)
nums = [1,2,3]
print(largestDivisibleSubset(nums))
nums = [1,2,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6,7,8,9,10,20,40,60,80,120,240]
print(largestDivisibleSubset(nums))
nums = [1]
print(largestDivisibleSubset(nums))
nums = [1,2]
print(largestDivisibleSubset(nums))
nums = [3,4,16,8]
print(largestDivisibleSubset(nums))
nums = [4,8,10,240]
print(largestDivisibleSubset(nums))
nums = [5,9,18,54,108,540,90,180,360,720]
print(largestDivisibleSubset(nums))
nums = [2,3,4,8]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6,7,8,9,10,20,40,60,80,120,240]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6,7,8,9,10,20,40,60,80,120,240]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6,7,8,9,10,20,40,60,80,120,240]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6,7,8,9,10,20,40,60,80,120,240]
print(largestDivisibleSubset(nums))
nums = [1,2,3,4,5,6

if __name__ == '__main__':
    largestDivisibleSubset()