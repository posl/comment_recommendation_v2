def twoSum(nums, target):
    index = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                if nums[i] + nums[j] == target:
                    index.append(i)
                    index.append(j)
                    return index
    return index

if __name__ == '__main__':
    twoSum()