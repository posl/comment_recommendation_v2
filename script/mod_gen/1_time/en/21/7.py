def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    diff = nums[1] - nums[0]
    count = 0
    slice_len = 2
    for i in range(2, len(nums)):
        if nums[i] - nums[i - 1] == diff:
            slice_len += 1
        else:
            if slice_len > 2:
                count += (slice_len - 1) * (slice_len - 2) / 2
            diff = nums[i] - nums[i - 1]
            slice_len = 2
    if slice_len > 2:
        count += (slice_len - 1) * (slice_len - 2) / 2
    return int(count)

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)