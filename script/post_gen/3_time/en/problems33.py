Synthesizing 10/10 solutions

=======
Suggestion 1

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

=======
Suggestion 2

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # Time Complexity: O(n^2)
    # Space Complexity: O(n^2)
    # dp[i][d] = # of subsequences ending at i with difference d
    # dp[i][d] = sum(dp[j][d]) + 1
    # ans = sum(dp[i][d])
    n = len(nums)
    dp = [{} for _ in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            d = nums[i] - nums[j]
            dp[i][d] = dp[i].get(d, 0) + dp[j].get(d, 0) + 1
            ans += dp[j].get(d, 0)
    return ans

=======
Suggestion 3

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 3:
        return 0
    dp = [{} for _ in range(len(nums))]
    result = 0
    for i in range(1, len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                result += dp[j][diff]
            else:
                dp[i][diff] = 1
    return result

=======
Suggestion 4

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    if n < 3:
        return 0
    dp = [{} for _ in range(n)]
    res = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                res += dp[j][diff]
            else:
                dp[i][diff] = 1
    return res

=======
Suggestion 5

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
print(numberOfArithmeticSlices([1,2,3,4,5]))
print(numberOfArithmeticSlices([1,2,3,4,5,6]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]))
print(numberOfArithmeticSlices([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]))
print(numberOfArithmeticSlices([1,2,3,

=======
Suggestion 6

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    n = len(nums)
    dp = [{} for i in range(n)]
    ans = 0
    for i in range(1, n):
        for j in range(i):
            diff = nums[i] - nums[j]
            if diff in dp[j]:
                dp[i][diff] = dp[j][diff] + 1
                ans += dp[j][diff]
            else:
                dp[i][diff] = 1
    return ans

print(numberOfArithmeticSlices([2,4,6,8,10]))
print(numberOfArithmeticSlices([7,7,7,7,7]))

=======
Suggestion 7

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    #The key is to find the difference between two consecutive elements
    #Then use the difference as key and the number of arithmetic sequences as value in a dictionary
    #Initialize the dictionary with the first two elements of the array
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is 0
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element
    #If the difference between the third element and the second element is the same as the difference between the second element and the first element, then the number of arithmetic sequences is the number of arithmetic sequences of the second element plus 1
    #If the difference between the third element and the second element is not the same as the difference

=======
Suggestion 8

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    total = 0
    dp = [{} for item in nums]
    for i in range(len(nums)):
        for j in range(i):
            diff = nums[i] - nums[j]
            dp[i][diff] = dp[i].get(diff, 0) + 1
            if diff in dp[j]:
                dp[i][diff] += dp[j][diff]
                total += dp[j][diff]
    return total

=======
Suggestion 9

def numberOfArithmeticSlices(nums):
    n = len(nums)
    dp = [defaultdict(int) for _ in range(n)]
    ans = 0
    for i in range(n):
        for j in range(i):
            d = nums[i] - nums[j]
            cnt = dp[j][d]
            ans += cnt
            dp[i][d] += cnt + 1
    return ans

=======
Suggestion 10

def numberOfArithmeticSlices(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    # TLE
    # def isArithmetic(l):
    #     for i in range(2, len(l)):
    #         if l[i] - l[i-1] != l[1] - l[0]:
    #             return False
    #     return True
    #
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if isArithmetic(l):
    #         return 1
    #     else:
    #         return helper(l[:-1]) + helper(l[1:])
    #
    # return helper(nums)

    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)

    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)

    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[2:])
    #     else:
    #         return helper(l[1:])
    #
    # return helper(nums)

    # TLE
    # def helper(l):
    #     if len(l) < 3:
    #         return 0
    #     if l[2] - l[1] == l[1] - l[0]:
    #         return 1 + helper(l[1:]) + helper(l[
