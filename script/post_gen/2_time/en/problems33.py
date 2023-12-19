Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][diff] stores the number of arithmetic subsequences ending at index i with difference diff
    # diff can be negative
    # dp[i][diff] = sum(dp[j][diff]) + 1 where j < i and diff = nums[i] - nums[j]
    # Since diff can be negative, we use a hashmap to store the number of arithmetic subsequences ending at index i with difference diff
    # dp[i][diff] = dp[j][diff] + 1 where j < i and diff = nums[i] - nums[j]
    # ans = sum(dp[i][diff]) where i = 0 to n - 1 and diff ranges from -2^31 to 2^31 - 1
    # We can use a 2D array to store dp[i][diff] where diff ranges from -2^31 to 2^31 - 1
    # But the space complexity would be O(n^2)
    # We can use a hashmap to store dp[i][diff] where diff ranges from -2^31 to 2^31 - 1
    # The space complexity would be O(n^2)

    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0

    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            ans += dp[j].get(diff, 0)

    return ans

=======
Suggestion 2

def numArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [{} for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            count += dp[j].get(diff, 0)
    return count

nums = [2,4,6,8,10]
print(numArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numArithmeticSlices(nums))

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(0, len(nums)-2):
        for j in range(i+1, len(nums)-1):
            diff = nums[j] - nums[i]
            for k in range(j+1, len(nums)):
                if nums[k] - nums[j] == diff:
                    count += 1
                elif nums[k] - nums[j] > diff:
                    break
    return count

nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                ans += dp[j][diff]
    return ans

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [dict() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            sum = dp[j].get(d, 0)
            origin = dp[i].get(d, 0)
            dp[i][d] = origin + sum + 1
            ans += sum
    return ans

nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))
nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    ans = 0
    dp = [defaultdict(int) for _ in range(n)]
    for i in range(n):
        for j in range(i):
            delta = nums[i] - nums[j]
            dp[i][delta] += 1
            if delta in dp[j]:
                dp[i][delta] += dp[j][delta]
                ans += dp[j][delta]
    return ans

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Solution 1:
    # Time Complexity: O(N^3)
    # Space Complexity: O(1)
    # if len(nums) < 3:
    #     return 0
    # res = 0
    # for i in range(len(nums) - 2):
    #     for j in range(i + 1, len(nums) - 1):
    #         diff = nums[j] - nums[i]
    #         for k in range(j + 1, len(nums)):
    #             if nums[k] - nums[j] == diff:
    #                 res += 1
    # return res

    # Solution 2:
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)
    # if len(nums) < 3:
    #     return 0
    # res = 0
    # dp = [{} for _ in range(len(nums))]
    # for i in range(1, len(nums)):
    #     for j in range(i):
    #         diff = nums[i] - nums[j]
    #         if diff in dp[j]:
    #             dp[i][diff] = dp[j][diff] + 1
    #             res += dp[j][diff]
    #         else:
    #             dp[i][diff] = 1
    # return res

    # Solution 3:
    # Time Complexity: O(N^2)
    # Space Complexity: O(N^2)
    if len(nums) < 3:
        return 0
    res = 0
    dp = [{} for _ in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                res += dp[j][diff]
            else:
                dp[i][diff] = 1
    return res

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^3)
    # Space Complexity: O(n^2)
    n = len(nums)
    dp = [dict() for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                ans += dp[j][diff]
    return ans

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [{} for i in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            if d in dp[j]:
                dp[i][d] = dp[j][d] + 1
                ans += dp[j][d]
            else:
                dp[i][d] = 1
    return ans

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([2,4,6,8,10,12]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26,28]))
print(numberOfArithmeticSlices([2,4,6,8,10,12,14,16,18,20,22,24,26,28,30]))
print(numberOfArithmeticSlices([2,4,6,8,10,

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [collections.defaultdict(int) for _ in range(n)]
    res = 0
    for i in range(n):
        for j in range(i):
            dp[i][nums[i] - nums[j]] += 1
            if nums[i] - nums[j] in dp[j]:
                dp[i][nums[i] - nums[j]] += dp[j][nums[i] - nums[j]]
                res += dp[j][nums[i] - nums[j]]
    return res

nums = [2,4,6,8,10]
print(numberOfArithmeticSlices(nums))

nums = [7,7,7,7,7]
print(numberOfArithmeticSlices(nums))
