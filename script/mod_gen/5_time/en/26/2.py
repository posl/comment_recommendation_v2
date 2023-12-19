def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    def splitArrayHelper(nums, m, mid):
        count = 1
        currentSum = 0
        for num in nums:
            currentSum += num
            if currentSum > mid:
                currentSum = num
                count += 1
                if count > m:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) / 2
        if splitArrayHelper(nums, m, mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()