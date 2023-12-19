def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def isPossible(mid, m, nums):
        count = 1
        sum = 0
        for num in nums:
            sum += num
            if sum > mid:
                count += 1
                sum = num
        return count <= m
    
    l = max(nums)
    r = sum(nums)
    while l < r:
        mid = l + (r - l)//2
        if isPossible(mid, m, nums):
            r = mid
        else:
            l = mid + 1
    return l
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print("The values above should be 18, 9, and 4.")

if __name__ == '__main__':
    splitArray()