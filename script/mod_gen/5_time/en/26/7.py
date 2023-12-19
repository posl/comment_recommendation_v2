def splitArray(nums, k):
    def check(m):
        cuts = 0
        current_sum = 0
        for num in nums:
            current_sum += num
            if current_sum > m:
                cuts += 1
                current_sum = num
        return cuts + 1 <= k
    left, right = max(nums), sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()