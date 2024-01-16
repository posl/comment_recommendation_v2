Synthesizing 10/10 solutions

=======
Suggestion 1

def splitArray(self, nums: list[int], k: int) -> int:
        pass

=======
Suggestion 2

def splitArray(self, nums: list[int], k: int) -> int:
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if self.valid(nums, k, mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 3

def splitArray(self, nums: list[int], k: int) -> int:
        # Time: O(nlog(sum(nums)) - n) Space: O(1)
        def isValid(target):
            count = 1
            currSum = 0
            for num in nums:
                currSum += num
                if currSum > target:
                    count += 1
                    currSum = num
            return count <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if isValid(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 4

def splitArray(self, nums: list[int], k: int) -> int:
        # binary search
        def possible(target):
            total, count = 0, 1
            for num in nums:
                total += num
                if total > target:
                    total = num
                    count += 1
                    if count > k:
                        return False
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if possible(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 5

def splitArray(self, nums: list[int], k: int) -> int:
        def check(x, k):
            cuts = 0
            curr_sum = 0
            for num in nums:
                if curr_sum + num > x:
                    cuts += 1
                    curr_sum = num
                else:
                    curr_sum += num
            return cuts <= k
        
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid, k):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 6

def splitArray(self, nums: list[int], k: int) -> int:
        def canSplit(maxSum: int) -> bool:
            splits = 1
            currSum = 0
            for num in nums:
                currSum += num
                if currSum > maxSum:
                    splits += 1
                    currSum = num
            return splits <= k
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            middle = left + (right - left) // 2
            if canSplit(middle):
                right = middle
            else:
                left = middle + 1
        return left

=======
Suggestion 7

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            cuts, curr_sum = 0, 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    cuts, curr_sum = cuts + 1, num
            return cuts + 1 <= k
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 8

def splitArray(self, nums: list[int], k: int) -> int:
        def isPossible(mid):
            cuts, currSum = 0, 0
            for num in nums:
                currSum += num
                if currSum > mid:
                    cuts, currSum = cuts + 1, num
                    if cuts > k:
                        return False
            return True
        left, right = max(nums), sum(nums)
        while left < right:
            mid = (left + right) // 2
            if isPossible(mid):
                right = mid
            else:
                left = mid + 1
        return left

=======
Suggestion 9

class Solution:
    def splitArray(self, nums: list[int], k: int) -> int:
        # 1. Binary search
        # 2. Greedy
        # 3. DP
        # 4. DFS
        # 5. BFS
        # 6. Sliding window
        # 7. Two pointers
        # 8. Stack
        # 9. Heap
        # 10. Math
        # 11. Union find
        # 12. Trie
        # 13. Design
        # 14. Topological sort
        # 15. Bit manipulation
        # 16. Random
        # 17. Rejection sampling
        # 18. Reservoir sampling
        # 19. Divide and conquer
        # 20. Recursion
        # 21. Memoization
        # 22. Geometry
        # 23. String
        # 24. Simulation
        # 25. Graph
        # 26. Tree
        # 27. Binary search tree
        # 28. Stack
        # 29. Heap
        # 30. Hash table
        # 31. Two pointers
        # 32. Sort
        # 33. Math
        # 34. Bit manipulation
        # 35. Union find
        # 36. Design
        # 37. Topological sort
        # 38. Trie
        # 39. Recursion
        # 40. Memoization
        # 41. Divide and conquer
        # 42. Geometry
        # 43. String
        # 44. Simulation
        # 45. Graph
        # 46. Tree
        # 47. Binary search tree
        # 48. Stack
        # 49. Heap
        # 50. Hash table
        # 51. Two pointers
        # 52. Sort
        # 53. Math
        # 54. Bit manipulation
        # 55. Union find
        # 56. Design
        # 57. Topological sort
        # 58. Trie
        # 59. Recursion
        # 60. Memoization
        # 61. Divide and conquer
        # 62. Geometry
        # 63. String
        # 64. Simulation
        # 65. Graph
        #

=======
Suggestion 10

def splitArray(self, nums: list[int], k: int) -> int:
        def check(mid):
            cuts = 0
            curr_sum = 0
            for num in nums:
                curr_sum += num
                if curr_sum > mid:
                    cuts += 1
                    curr_sum = num
            return cuts + 1 <= k
        
        left = max(nums)
        right = sum(nums)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left
