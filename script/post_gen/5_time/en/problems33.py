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
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            c1 = dp[j].get(d, 0)
            c2 = dp[i].get(d, 0)
            ans += c1
            dp[i][d] = c1 + c2 + 1
    return ans

=======
Suggestion 3

def arithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    dp = [{} for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res

nums = [2,4,6,8,10]
print(arithmeticSlices(nums))
nums = [7,7,7,7,7]
print(arithmeticSlices(nums))

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    result = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            diff = nums[j] - nums[i]
            count = 2
            for k in range(j+1, n):
                if nums[k] - nums[j] == diff:
                    count += 1
            if count >= 3:
                result += 1
    return result

=======
Suggestion 5

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            ans += dp[j].get(diff, 0)
    return ans

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(1, len(nums) - 1):
        for j in range(i + 1, len(nums)):
            if nums[j] - nums[i] == nums[i] - nums[i - 1]:
                count += 1
            else:
                break
    return count

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    res = 0
    dp = [{} for i in range(len(nums))]
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)
    return res

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    count = 0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            diff = nums[j] - nums[i]
            prev = nums[j]
            for k in range(j+1,len(nums)):
                if nums[k] - prev == diff:
                    count += 1
                    prev = nums[k]
    return count

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [{} for _ in range(len(nums))]
    res = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[i]:
                dp[i][diff] += 1
            else:
                dp[i][diff] = 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                res += dp[j][diff]
    return res

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print("The values above should be 7, 16, and 10.")

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0

    # dp[i][j] stores the number of arithmetic slices ending at index i with difference j
    dp = [{} for _ in range(len(nums))]
    res = 0

    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + dp[j].get(diff, 0) + 1
            res += dp[j].get(diff, 0)

    return res

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,1,1,1,1]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,3,5,7,9]))
print(numberOfArithmeticSlices([7,3,5,1,9]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35]))
print(numberOfArithmeticSlices([1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37]))
print(numberOfArithmeticSlices([1,3,5,7,
