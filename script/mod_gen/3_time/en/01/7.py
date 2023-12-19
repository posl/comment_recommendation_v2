def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i!=j) and (nums[i]+nums[j]==target):
                return [i,j]
    return None

if __name__ == '__main__':
    twoSum()