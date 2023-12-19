def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums)<3:
        return 0
    count=0
    for i in range(0,len(nums)-2):
        d=nums[i+1]-nums[i]
        for j in range(i+2,len(nums)):
            if nums[j]-nums[j-1]==d:
                count+=1
            else:
                break
    return count
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print("The values above should be 3, 0, and 36.")

if __name__ == '__main__':
    numberOfArithmeticSlices()