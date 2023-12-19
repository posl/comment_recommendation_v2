def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    def check(mid):
        count = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                curr_sum = num
                count += 1
                if count > k:
                    return False
        return True
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) / 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left
print(splitArray([7,2,5,10,8], 2))
print(splitArray([1,2,3,4,5], 2))
print(splitArray([1,4,4], 3))
print("The values above should be 18, 9, and 4.")

if __name__ == '__main__':
    splitArray()