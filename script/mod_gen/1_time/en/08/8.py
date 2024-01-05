def rotate(nums, k):
    """
    Rotate the array to the right by k steps, where k is non-negative.
    Do not return anything, modify nums in-place instead.
    """
    #nums.reverse()
    #nums[:k] = reversed(nums[:k])
    #nums[k:] = reversed(nums[k:])
    k = k % len(nums)
    nums[:k], nums[k:] = nums[len(nums)-k:], nums[:len(nums)-k]
    return nums

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    k = int(input())
    a = rotate(nums, k)
    print(a)