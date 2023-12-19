def splitArray(self, nums: List[int], k: int) -> int:
    # Time: O(nlog(sum of nums))
    # Space: O(1)
    # Binary search on the answer. The answer lies between the max element and the sum of all elements
    # We need to find the min sum of subarrays such that the number of subarrays is equal to k
    # We can use binary search to find the answer. We can use the greedy approach to find the min sum of subarrays
    # We can check if the mid value is possible or not. If it is possible, we can try to find a better answer
    # If it is not possible, we can increase the mid value
    # The answer will be the minimum value of mid such that it is possible to get k subarrays
    # We can use a greedy approach to check if the mid value is possible or not
    # We can keep a track of the sum of the subarray and the number of subarrays
    # If the sum of the subarray exceeds the mid value, we can increase the number of subarrays
    # We can also check if the number of subarrays is greater than k or not
    # If the number of subarrays is greater than k, we can return False
    # If the number of subarrays is less than or equal to k, we can return True
    def isPossible(mid, k):
        subarraySum = 0
        subarrays = 1
        for num in nums:
            subarraySum += num
            if subarraySum > mid:
                subarraySum = num
                subarrays += 1
                if subarrays > k:
                    return False
        return True
    low = max(nums)
    high = sum(nums)
    while low < high:
        mid = low + (high - low) // 2
        if isPossible(mid, k):
            high = mid
        else:
            low = mid + 1
    return low

if __name__ == '__main__':
    splitArray()