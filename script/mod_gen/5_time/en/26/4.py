def splitArray(nums, m):
    """
    :type nums: List[int]
    :type m: int
    :rtype: int
    """
    # this is a binary search problem
    # the max possible sum is sum(nums)
    # the min possible sum is max(nums)
    # we want to find the minimum possible sum of the largest sum of subarrays
    # we can binary search between max(nums) and sum(nums)
    # if the current sum is too small, we need to increase the max sum
    # if the current sum is too large, we need to decrease the max sum
    # if the current sum is just right, we need to check if we can decrease the max sum
    # we can do this by checking if the number of subarrays we have is less than or equal to m
    # if it is, we can decrease the max sum
    # if it is not, we need to increase the max sum
    # if we reach the point where the max sum and min sum are equal, we can return that sum
    # we can check if the sum is too small or too large by using a helper function
    # the helper function will return the number of subarrays we have if we use the current sum
    # if the number of subarrays is less than or equal to m, we can decrease the max sum
    # if the number of subarrays is greater than m, we can increase the max sum
    # we can start by setting the max sum to the sum of the array and the min sum to the max of the array
    # we can then binary search between the min sum and the max sum
    # if the max sum and min sum are equal, we can return the sum
    # we can check if the sum is too small or too large by using a helper function
    # the helper function will return the number of subarrays we have if we use the current sum
    # if the number of subarrays is less than or equal to m, we can decrease the max sum
    # if the number of subarrays is greater than m, we can increase the max sum
    # we can do this by using a binary search
    # we can start by setting the max sum to the sum of the array and the min sum to the max of the array
    # we can then binary search

if __name__ == '__main__':
    splitArray()