Synthesizing 10/10 solutions

=======
Suggestion 1

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        result = 0
        for i in range(len(nums) - 2):
            j = i + 1
            diff = nums[j] - nums[i]
            while j < len(nums) - 1 and nums[j + 1] - nums[j] == diff:
                j += 1
            if j - i + 1 >= 3:
                result += ((j - i) * (j - i + 1)) // 2
                i = j
        return result

=======
Suggestion 2

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Brute force
        # Time: O(n^3)
        # Space: O(1)
        #count = 0
        #for i in range(len(nums)):
        #    for j in range(i+1, len(nums)):
        #        if j - i == 1:
        #            continue
        #        diff = nums[j] - nums[j-1]
        #        k = j
        #        while k < len(nums) and nums[k] - nums[k-1] == diff:
        #            k += 1
        #        if k - j >= 2:
        #            count += 1
        #return count

        # Brute force
        # Time: O(n^2)
        # Space: O(1)
        #count = 0
        #for i in range(len(nums)):
        #    diff = nums[i] - nums[i-1]
        #    for j in range(i+1, len(nums)):
        #        if nums[j] - nums[j-1] == diff:
        #            count += 1
        #        else:
        #            break
        #return count

        # Dynamic programming
        # Time: O(n)
        # Space: O(1)
        count = 0
        dp = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp += 1
                count += dp
            else:
                dp = 0
        return count

        # Dynamic programming
        # Time: O(n)
        # Space: O(n)
        #count = 0
        #dp = [0] * len(nums)
        #for i in range(2, len(nums)):
        #    if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
        #        dp[i] = dp[i-1] + 1
        #        count += dp[i]
        #return count

        # Brute force
        # Time: O(n)
        # Space: O(n)
        #count = 0
        #dp = [0] * len(nums)
        #for i in range(2, len(nums)):
        #    if nums[i

=======
Suggestion 3

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                count += 1
        return count

=======
Suggestion 4

class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # 1. Brute Force
        # 2. DP
        # 3. Constant Space
        # 4. Math
        # 5. Sliding Window
        # 6. Two Pointers
        # 7. Stack
        # 8. Sorting
        # 9. Greedy
        # 10. Divide and Conquer
        # 11. Backtracking
        # 12. Bit Manipulation
        # 13. Recursion
        # 14. Hashing
        # 15. Binary Search
        # 16. Tree
        # 17. Trie
        # 18. Heap
        # 19. Graph
        # 20. Union Find
        # 21. Design
        # 22. Topological Sort
        # 23. Segment Tree
        # 24. Binary Indexed Tree
        # 25. Line Sweep
        # 26. Random
        # 27. Rejection Sampling
        # 28. Reservoir Sampling
        # 29. Rolling Hash
        # 30. Suffix Array
        # 31. Geometry
        # 32. Brainteaser
        # 33. Memoization
        # 34. Queue
        # 35. Minimax
        # 36. Ordered Map
        # 37. Geometry
        # 38. Sliding Window
        # 39. Random
        # 40. Binary Search
        # 41. Prefix Sum
        # 42. Simulation
        # 43. Stack
        # 44. Math
        # 45. String
        # 46. Binary Search Tree
        # 47. Trie
        # 48. Depth-First Search
        # 49. Breadth-First Search
        # 50. Greedy
        # 51. Sort
        # 52. Bit Manipulation
        # 53. Hash Table
        # 54. Two Pointers
        # 55. Stack
        # 56. Math
        # 57. String
        # 58. Dynamic Programming
        # 59. Tree
        # 60. Depth-First Search
        # 61. Breadth-First Search
        # 62. Binary Search

=======
Suggestion 5

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        count = 0
        for i in range(len(nums)-2):
            diff = nums[i+1] - nums[i]
            for j in range(i+2, len(nums)):
                if nums[j] - nums[j-1] == diff:
                    count += 1
                else:
                    break
        return count

=======
Suggestion 6

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        #Time: O(n)
        #Space: O(1)
        count = 0
        for i in range(1, len(nums)-1):
            if nums[i] - nums[i-1] == nums[i+1] - nums[i]:
                count += 1
        return count

=======
Suggestion 7

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        dp = [0]*n
        for i in range(2,n):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dp[i] = dp[i-1] + 1
        return sum(dp)

=======
Suggestion 8

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        ans = 0
        diff = nums[1] - nums[0]
        count = 1
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                count += 1
            else:
                if count >= 2:
                    ans += (count - 1) * count // 2
                diff = nums[i] - nums[i - 1]
                count = 1
        if count >= 2:
            ans += (count - 1) * count // 2
        return ans

=======
Suggestion 9

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # Solution 1 - 40 ms
        """
        dp = [0] * len(nums)
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1

        return sum(dp)
        """
        # Solution 2 - 16 ms
        if len(nums) < 3:
            return 0
        ans = 0
        count = 0
        diff = nums[1] - nums[0]
        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == diff:
                count += 1
            else:
                diff = nums[i] - nums[i - 1]
                count = 0
            ans += count
        return ans

=======
Suggestion 10

def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        if len(nums) < 3:
            return 0
        difference = nums[1] - nums[0]
        count = 0
        length = 2
        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == difference:
                length += 1
            else:
                if length > 2:
                    count += (length - 1) * (length - 2) // 2
                difference = nums[i] - nums[i-1]
                length = 2
        if length > 2:
            count += (length - 1) * (length - 2) // 2
        return count
