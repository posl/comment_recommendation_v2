def twoSum(nums, target):
    for i in range(0, len(nums)):
        for j in range(i+1, len(nums)):
            if (nums[i]+nums[j] == target):
                return [i, j]
    return []

if __name__ == '__main__':
    twoSum()