def rotate(nums):
    return [nums[-1]] + nums[:-1]

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = rotate(nums)
    print(a)