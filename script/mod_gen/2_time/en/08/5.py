def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    temp = [0]*len(nums)
    for i in range(len(nums)):
        temp[(i+k)%len(nums)] = nums[i]
    for i in range(len(nums)):
        nums[i] = temp[i]

if __name__ == '__main__':
    rotate()