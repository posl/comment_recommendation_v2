def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) == 1:
        return 0
    else:
        max_val = 0
        for i in range(len(nums)):
            if i == 0:
                max_val = sum([nums[j]*j for j in range(len(nums))])
            else:
                nums = [nums[-1]] + nums[:-1]
                tmp = sum([nums[j]*j for j in range(len(nums))])
                if tmp > max_val:
                    max_val = tmp
        return max_val

if __name__ == '__main__':
    maxRotateFunction()