def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            diff = nums[j] - nums[i]
            count = 2
            for k in range(j+1, n):
                if nums[k] - nums[j] == diff:
                    count += 1
            if count >= 3:
                result += 1
    return result

if __name__ == '__main__':
    numberOfArithmeticSlices()