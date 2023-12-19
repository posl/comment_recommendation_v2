def largestDivisibleSubset(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # First sort the list
    nums.sort()
    # Create a list to store the length of the largest subset
    dp = [1] * len(nums)
    # Create a list to store the previous index of the largest subset
    prev = [-1] * len(nums)
    # Create a variable to store the index of the largest subset
    max_index = 0
    # Create a variable to store the length of the largest subset
    max_length = 0
    # Iterate through the list
    for i in range(len(nums)):
        # Iterate through the list
        for j in range(i):
            # If the current number is divisible by the previous number
            if nums[i] % nums[j] == 0:
                # If the length of the largest subset is less than the length of the previous subset + 1
                if dp[i] < dp[j] + 1:
                    # Update the length of the largest subset
                    dp[i] = dp[j] + 1
                    # Update the previous index of the largest subset
                    prev[i] = j
        # If the length of the largest subset is greater than the maximum length
        if max_length < dp[i]:
            # Update the maximum length
            max_length = dp[i]
            # Update the index of the maximum length
            max_index = i
    # Create a list to store the largest subset
    result = []
    # Iterate until the maximum index is not -1
    while max_index != -1:
        # Append the number at the maximum index to the list
        result.append(nums[max_index])
        # Update the maximum index
        max_index = prev[max_index]
    # Return the largest subset
    return result

if __name__ == '__main__':
    largestDivisibleSubset()