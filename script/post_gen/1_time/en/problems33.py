Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """

=======
Suggestion 2

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp[i][d] represents the number of arithmetic subsequences ending with nums[i] and its common difference is d.
    #dp[i][d] += dp[j][d] + 1, where j < i and nums[i] - nums[j] == d.
    #Time: O(n^2)
    #Space: O(n^2)
    dp = [dict() for _ in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
            res += dp[j].get(d, 0)
    return res

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][diff] represents the number of arithmetic subsequences with difference diff ending at index i.
    # dp[i][diff] = sum(dp[j][diff]) + 1, where j < i and diff == nums[i] - nums[j]
    # ans = sum(dp[i][diff]) for i in range(1, len(nums))
    # Note: it is also possible to solve this problem in O(n^2) time and O(n) space.
    # dp[i] represents the number of arithmetic subsequences ending at index i.
    # dp[i] = sum(dp[j]) + 1, where j < i and nums[i] - nums[j] == nums[j] - nums[k] and k < j
    # ans = sum(dp[i]) for i in range(1, len(nums))
    dp = [{} for _ in range(len(nums))]
    ans = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff not in dp[i]:
                dp[i][diff] = 0
            if diff not in dp[j]:
                dp[j][diff] = 0
            dp[i][diff] += dp[j][diff] + 1
            ans += dp[j][diff]
    return ans

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #dp = [collections.defaultdict(int) for _ in nums]
    dp = [{} for _ in nums]
    res = 0
    for i in range(len(nums)):
        for j in range(i):
            dp[i][nums[i] - nums[j]] = dp[i].get(nums[i] - nums[j], 0) + dp[j].get(nums[i] - nums[j], 0) + 1
            res += dp[j].get(nums[i] - nums[j], 0)
    return res

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # DP
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1, i - 2, ..., 0
    # d = nums[i] - nums[j]
    # dp[i][d] is the number of arithmetic subsequences
    # with difference d ending at index i
    # dp[i][d] = dp[j][d] + 1
    # j = i - 1

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1
    # Time:  O(n^2)
    # Space: O(n)
    # dp[i][j] = # of arithmetic subsequence slices of nums[:i+1] ending with nums[i] with difference nums[i]-nums[j]
    # dp[i][j] = sum(dp[j][k]) + 1, 0 <= k < j, if nums[i]-nums[j] == nums[j]-nums[k]
    #           1, otherwise
    #           0, if i < j
    # return sum(dp[i][j] for i in range(2, len(nums)) for j in range(i))
    # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    # result = 0
    # for i in range(2, len(nums)):
    #     for j in range(i):
    #         for k in range(j):
    #             if nums[i]-nums[j] == nums[j]-nums[k]:
    #                 dp[i][j] += dp[j][k] + 1
    #                 result += dp[j][k] + 1
    # return result

    # Solution 2
    # Time:  O(n^2)
    # Space: O(n^2)
    # dp[i][j] = # of arithmetic subsequence slices of nums[:i+1] ending with nums[i] with difference nums[i]-nums[j]
    # dp[i][j] = sum(dp[j][k]) + 1, 0 <= k < j, if nums[i]-nums[j] == nums[j]-nums[k]
    #           1, otherwise
    #           0, if i < j
    # return sum(dp[i][j] for i in range(2, len(nums)) for j in range(i))
    # dp = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
    # result = 0
    # for i in range(2, len(nums)):
    #     for j in range(i):
    #         for k in range(j):
    #             if nums[i]-nums[j] == nums[j]-nums[k]:
    #                 dp[i][j]

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    n = len(nums)
    dp = [{} for i in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                res += dp[j][diff]
    return res

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    dp = [{} for i in nums]
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            count += dp[j].get(diff, 0)
    return count

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
print(numberOfArithmeticSlices([1,1,1,1,1,1,1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]))
print(number

=======
Suggestion 9

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

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # 1 <= nums.length <= 5000
    # -2^31 <= nums[i] <= 2^31 - 1
    # 1 <= nums[i] <= 5000
    # -5000 <= nums[i] <= 5000
    # 1 <= nums[i] <= 1000
    # -1000 <= nums[i] <= 1000
    # 1 <= nums[i] <= 2000
    # -2000 <= nums[i] <= 2000
    # 1 <= nums[i] <= 3000
    # -3000 <= nums[i] <= 3000
    # 1 <= nums[i] <= 4000
    # -4000 <= nums[i] <= 4000
    # 1 <= nums[i] <= 5000
    # -5000 <= nums[i] <= 5000
    # 1 <= nums[i] <= 6000
    # -6000 <= nums[i] <= 6000
    # 1 <= nums[i] <= 7000
    # -7000 <= nums[i] <= 7000
    # 1 <= nums[i] <= 8000
    # -8000 <= nums[i] <= 8000
    # 1 <= nums[i] <= 9000
    # -9000 <= nums[i] <= 9000
    # 1 <= nums[i] <= 10000
    # -10000 <= nums[i] <= 10000
    # 1 <= nums[i] <= 11000
    # -11000 <= nums[i] <= 11000
    # 1 <= nums[i] <= 12000
    # -12000 <= nums[i] <= 12000
    # 1 <= nums[i] <= 13000
    # -13000 <= nums[i] <= 13000
    # 1 <= nums[i] <= 14000
    # -14000 <= nums[i] <= 14000
    # 1 <= nums[i] <= 15000
    # -15000 <= nums[i] <= 15000
    # 1 <= nums[i] <= 16000
