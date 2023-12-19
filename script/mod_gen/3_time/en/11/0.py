def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # O(n^2) - Dynamic Programming
    # O(n) - Binary Search
    # The idea is to use an array to store the longest increasing subsequence
    # so far. The array is sorted from small to large. For each new item, we
    # do binary search to find the first item in the array which is larger than
    # the new item. If there is no such item, we append the new item to the
    # array. Otherwise, we replace the first item which is larger than the new
    # item with the new item.
    # The size of the array is the length of the longest increasing subsequence
    # so far.
    # Reference: https://www.youtube.com/watch?v=1RpMc3fv0y4
    # Time: O(nlogn)
    # Space: O(n)
    if not nums:
        return 0
    dp = []
    for num in nums:
        if not dp or num > dp[-1]:
            dp.append(num)
        else:
            left = 0
            right = len(dp) - 1
            while left < right:
                mid = (left + right) // 2
                if dp[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            dp[left] = num
    return len(dp)

if __name__ == '__main__':
    lengthOfLIS()