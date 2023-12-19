def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #brute force
    #create a list of all possible slices
    #check if the difference between each slice is the same
    #return the number of slices that have the same difference
    #O(n^2) time complexity and O(1) space complexity
    #slices = []
    #for i in range(len(nums)):
    #    for j in range(i+1, len(nums)):
    #        slices.append(nums[i:j+1])
    #count = 0
    #for s in slices:
    #    if len(s) < 3:
    #        continue
    #    diff = s[1] - s[0]
    #    for i in range(1, len(s)-1):
    #        new_diff = s[i+1] - s[i]
    #        if new_diff != diff:
    #            break
    #    else:
    #        count += 1
    #return count
    #dynamic programming
    #O(n^2) time complexity and O(n) space complexity
    #dp = [{} for _ in range(len(nums))]
    #count = 0
    #for i in range(1, len(nums)):
    #    for j in range(i):
    #        diff = nums[i] - nums[j]
    #        temp = dp[j].get(diff, 0)
    #        dp[i][diff] = dp[i].get(diff, 0) + temp + 1
    #        count += temp
    #return count
    #dynamic programming
    #O(n^2) time complexity and O(n) space complexity
    dp = [{} for _ in range(len(nums))]
    count = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            temp = dp[j].get(diff, 0)
            dp[i][diff] = dp[i].get(diff, 0) + temp + 1
            count += temp
    return count

if __name__ == '__main__':
    numberOfArithmeticSlices()