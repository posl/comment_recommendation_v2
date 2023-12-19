def slices(nums):
    count = 0
    for i in range(len(nums)-2):
        if nums[i+2] - nums[i+1] == nums[i+1] - nums[i]:
            count += 1
    return count

if __name__ == '__main__':
    slices()