def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    l = len(nums)
    k = k % l
    if k == 0:
        return nums
    nums[:] = nums[l-k:] + nums[:l-k]
    return nums

if __name__ == '__main__':
    rotate()