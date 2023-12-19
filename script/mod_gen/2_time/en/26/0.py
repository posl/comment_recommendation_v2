def splitArray(self, nums: List[int], k: int) -> int:
    def check(mid):
        count = 1
        curr_sum = 0
        for num in nums:
            curr_sum += num
            if curr_sum > mid:
                curr_sum = num
                count += 1
                if count > k:
                    return False
        return True
    left = max(nums)
    right = sum(nums)
    while left < right:
        mid = left + (right - left) // 2
        if check(mid):
            right = mid
        else:
            left = mid + 1
    return left

if __name__ == '__main__':
    splitArray()