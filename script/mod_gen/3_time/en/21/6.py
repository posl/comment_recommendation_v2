def arithmeticSlices(nums):
    count = 0
    for i in range(len(nums)-2):
        if nums[i+1] - nums[i] == nums[i+2] - nums[i+1]:
            count += 1
            j = 3
            while i+j < len(nums) and nums[i+j] - nums[i+j-1] == nums[i+1] - nums[i]:
                count += 1
                j += 1
    return count
nums = [1, 2, 3, 4]
print(arithmeticSlices(nums))
nums = [1]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20]
print(arithmeticSlices(nums))
nums = [1, 2, 3, 4, 5, 6, 8, 10, 12, 14, 16, 17, 18, 19, 20, 21]
print(arithmeticSlices(nums))
nums = [1, 3, 5, 7, 9]
print(arithmeticSlices(nums))
nums = [7, 7, 7, 7]
print(arithmetic

if __name__ == '__main__':
    arithmeticSlices()