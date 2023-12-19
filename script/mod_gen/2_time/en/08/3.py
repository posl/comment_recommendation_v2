def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    if k == 0 or len(nums) == 1:
        return
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]

if __name__ == '__main__':
    rotate()