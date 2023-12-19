def maxRotateFunction(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum(nums) - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result
    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result
    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result
    #result = 0
    #for i in range(0, len(nums)):
    #    result += i * nums[i]
    #sum_nums = sum(nums)
    #max_result = result
    #for i in range(0, len(nums)):
    #    result = result + sum_nums - len(nums) * nums[-i-1]
    #    max_result = max(max_result, result)
    #return max_result
    result = 0
    for i in range(0, len(nums)):
        result += i * nums[i]
    sum_nums = sum(nums)
    max_result = result
    for i in range(0, len(nums)):
        result = result + sum_nums - len(nums) * nums[-i-1]
        max_result = max(max_result, result)
    return max_result
print(maxRotateFunction([4,3,2,6]))
print(maxRotateFunction([100]))
print(maxRotateFunction([1
