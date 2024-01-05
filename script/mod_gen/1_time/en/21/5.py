def numberOfArithmeticSlices(nums):
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if(nums[i:j+1] == sorted(nums[i:j+1])):
                count += 1
    return count
nums = [1,2,3,4]
print(numberOfArithmeticSlices(nums))
nums = [1]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(numberOfArithmeticSlices(nums))
nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)