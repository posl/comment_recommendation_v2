def findArithmeticSubarrays(nums):
    def isArithmetic(array):
        if len(array) < 3:
            return False
        diff = array[1] - array[0]
        for i in range(1, len(array) - 1):
            if array[i + 1] - array[i] != diff:
                return False
        return True
    count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if isArithmetic(nums[i:j + 1]):
                count += 1
    return count
print(findArithmeticSubarrays([1,2,3,4]))
print(findArithmeticSubarrays([1]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]))
print(findArithmeticSubarrays([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
