def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    for i in range(k):
        nums.insert(0,nums.pop())

if __name__ == '__main__':
    rotate()