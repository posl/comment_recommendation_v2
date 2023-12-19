def splitArray(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: int
    """
    # The idea is to use binary search to search the answer.
    # The answer is between max(nums) and sum(nums)
    # We use binary search to find the smallest sum that is 
    # greater than max(nums) and less than sum(nums)
    def is_valid(nums, k, mid):
        # This function checks if we can split nums into k subarrays
        # such that the sum of each subarray is less than or equal to mid
        # If we can, return True
        # Else, return False
        subarray_sum = 0
        num_subarrays = 1
        for num in nums:
            subarray_sum += num
            if subarray_sum > mid:
                # We have to start a new subarray
                num_subarrays += 1
                subarray_sum = num
                if num_subarrays > k:
                    # We can't split nums into k subarrays
                    return False
        return True
    
    # Initialize the left and right pointers
    left = max(nums)
    right = sum(nums)
    # Binary search
    while left < right:
        mid = left + (right - left) // 2
        if is_valid(nums, k, mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()