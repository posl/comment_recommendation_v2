def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    count = 0
    for i in range(len(nums) - 2):
        for j in range(i + 1, len(nums) - 1):
            diff = nums[j] - nums[i]
            for k in range(j + 1, len(nums)):
                if nums[k] - nums[j] == diff:
                    count += 1
                elif nums[k] - nums[j] > diff:
                    break
    return count

if __name__ == '__main__':
    nums = list(map(int, input().split()))
    a = numberOfArithmeticSlices(nums)
    print(a)