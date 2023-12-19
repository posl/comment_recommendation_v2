def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                print([i, j])
                return [i, j]

if __name__ == '__main__':
    twoSum()